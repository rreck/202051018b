#!/usr/bin/env python3
"""
Fraud Simulation API Extension
Extends A2A API with run-based fraud simulation endpoints
"""

import json
import logging
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict
from urllib.parse import urlparse, parse_qs

from run_manager import RunManager


class FraudSimMetrics:
    """Thread-safe metrics for fraud simulation runs"""
    def __init__(self):
        self._lock = threading.Lock()
        self._metrics = {
            'runs_total': 0,
            'runs_in_progress': 0,
            'runs_completed': 0,
            'runs_failed': 0,
            'last_run_accuracy': 0.0,
            'last_run_precision': 0.0,
            'last_run_recall': 0.0,
            'last_run_f1_score': 0.0,
            'total_transactions_analyzed': 0,
            'total_fraud_detected': 0,
            'pattern_flags': {}
        }
        self._run_history = []  # Store last 100 runs for comparison

    def increment(self, metric: str, value: float = 1.0):
        with self._lock:
            if metric in self._metrics:
                self._metrics[metric] += value

    def set_gauge(self, metric: str, value: float):
        with self._lock:
            self._metrics[metric] = value

    def update_pattern_flag(self, flag: str, count: int):
        with self._lock:
            self._metrics['pattern_flags'][flag] = count

    def add_run_result(self, run_id: str, fraud_type: str, accuracy: float, precision: float, recall: float, f1_score: float):
        """Track individual run results for comparison"""
        with self._lock:
            self._run_history.append({
                'run_id': run_id,
                'fraud_type': fraud_type,
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1_score,
                'timestamp': time.time()
            })
            # Keep only last 100 runs
            if len(self._run_history) > 100:
                self._run_history.pop(0)

    def get_metrics(self) -> Dict:
        with self._lock:
            return self._metrics.copy()

    def get_run_history(self) -> list:
        with self._lock:
            return self._run_history.copy()


FRAUD_SIM_METRICS = FraudSimMetrics()


class FraudSimAPIHandler(BaseHTTPRequestHandler):
    """Extended A2A API handler for fraud simulation"""

    def log_message(self, format, *args):
        pass  # Suppress HTTP logs

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == "/sim/status":
            self.handle_status()
        elif path == "/sim/runs":
            self.handle_list_runs()
        elif path.startswith("/sim/run/"):
            run_id = path.split("/sim/run/")[1]
            self.handle_get_run(run_id)
        elif path == "/sim/metrics":
            self.handle_metrics()
        else:
            self.send_error_response(404, "Endpoint not found")

    def do_POST(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
        except Exception as e:
            self.send_error_response(400, f"Invalid JSON: {e}")
            return

        if path == "/sim/run":
            self.handle_create_run(data)
        else:
            self.send_error_response(404, "Endpoint not found")

    def handle_status(self):
        """GET /sim/status - Get simulation system status"""
        metrics = FRAUD_SIM_METRICS.get_metrics()
        run_manager = getattr(self.server, 'run_manager', None)

        status = {
            'status': 'running',
            'runs_total': metrics['runs_total'],
            'runs_in_progress': metrics['runs_in_progress'],
            'runs_completed': metrics['runs_completed'],
            'runs_failed': metrics['runs_failed'],
            'timestamp': time.time()
        }

        if run_manager:
            status['available_runs'] = len(run_manager.list_runs())

        self.send_json_response(status)

    def handle_list_runs(self):
        """GET /sim/runs - List all simulation runs"""
        run_manager = getattr(self.server, 'run_manager', None)
        if not run_manager:
            self.send_error_response(500, "Run manager not initialized")
            return

        all_metrics = run_manager.get_all_metrics()
        runs = []

        for metrics in all_metrics:
            runs.append({
                'run_id': metrics.run_id,
                'fraud_type': metrics.fraud_type,
                'transaction_count': metrics.transaction_count,
                'fraud_count': metrics.fraud_count,
                'accuracy': metrics.accuracy,
                'precision': metrics.precision,
                'recall': metrics.recall,
                'f1_score': metrics.f1_score,
                'status': metrics.status,
                'timestamp': metrics.timestamp
            })

        self.send_json_response({
            'runs': runs,
            'total': len(runs)
        })

    def handle_get_run(self, run_id: str):
        """GET /sim/run/{run_id} - Get specific run details"""
        run_manager = getattr(self.server, 'run_manager', None)
        if not run_manager:
            self.send_error_response(500, "Run manager not initialized")
            return

        metrics = run_manager.get_run_metrics(run_id)
        if not metrics:
            self.send_error_response(404, f"Run not found: {run_id}")
            return

        import dataclasses
        self.send_json_response(dataclasses.asdict(metrics))

    def handle_create_run(self, data: Dict):
        """
        POST /sim/run - Create and execute new fraud simulation run

        Request body:
        {
            "fraud_type": "card_testing",
            "transaction_count": 1000,
            "fraud_intensity": 0.10,
            "detection_threshold": 75
        }
        """
        run_manager = getattr(self.server, 'run_manager', None)
        if not run_manager:
            self.send_error_response(500, "Run manager not initialized")
            return

        # Extract parameters
        fraud_type = data.get('fraud_type', 'card_testing')
        transaction_count = data.get('transaction_count', 1000)
        fraud_intensity = data.get('fraud_intensity', 0.10)
        detection_threshold = data.get('detection_threshold', 75)

        # Validate parameters
        valid_fraud_types = ['card_testing', 'velocity_attack', 'account_takeover', 'synthetic_identity']
        if fraud_type not in valid_fraud_types:
            self.send_error_response(400, f"Invalid fraud_type: {fraud_type}. Valid types: {valid_fraud_types}")
            return

        if not (100 <= transaction_count <= 100000):
            self.send_error_response(400, "transaction_count must be between 100 and 100000")
            return

        if not (0.0 <= fraud_intensity <= 1.0):
            self.send_error_response(400, "fraud_intensity must be between 0.0 and 1.0")
            return

        if not (0 <= detection_threshold <= 100):
            self.send_error_response(400, "detection_threshold must be between 0 and 100")
            return

        try:
            # Create run
            FRAUD_SIM_METRICS.increment('runs_total')
            FRAUD_SIM_METRICS.increment('runs_in_progress')

            run_id = run_manager.create_run(
                fraud_type=fraud_type,
                transaction_count=transaction_count,
                fraud_intensity=fraud_intensity,
                detection_threshold=detection_threshold
            )

            # Execute run (synchronous for now)
            metrics = run_manager.execute_run(run_id)

            # Update metrics
            FRAUD_SIM_METRICS.increment('runs_in_progress', -1)
            FRAUD_SIM_METRICS.increment('runs_completed')
            FRAUD_SIM_METRICS.set_gauge('last_run_accuracy', metrics.accuracy)
            FRAUD_SIM_METRICS.set_gauge('last_run_precision', metrics.precision)
            FRAUD_SIM_METRICS.set_gauge('last_run_recall', metrics.recall)
            FRAUD_SIM_METRICS.set_gauge('last_run_f1_score', metrics.f1_score)
            FRAUD_SIM_METRICS.increment('total_transactions_analyzed', metrics.transaction_count)
            FRAUD_SIM_METRICS.increment('total_fraud_detected', metrics.detected_count)

            # Track run history for comparison
            FRAUD_SIM_METRICS.add_run_result(
                run_id=metrics.run_id,
                fraud_type=metrics.fraud_type,
                accuracy=metrics.accuracy,
                precision=metrics.precision,
                recall=metrics.recall,
                f1_score=metrics.f1_score
            )

            for flag, count in metrics.pattern_flag_counts.items():
                FRAUD_SIM_METRICS.update_pattern_flag(flag, count)

            import dataclasses
            self.send_json_response({
                'status': 'completed',
                'run_id': run_id,
                'metrics': dataclasses.asdict(metrics)
            })

        except Exception as e:
            FRAUD_SIM_METRICS.increment('runs_in_progress', -1)
            FRAUD_SIM_METRICS.increment('runs_failed')
            logging.getLogger(__name__).error(f"Error creating run: {e}")
            self.send_error_response(500, f"Error creating run: {str(e)}")

    def handle_metrics(self):
        """GET /sim/metrics - Get Prometheus-format metrics"""
        metrics = FRAUD_SIM_METRICS.get_metrics()
        run_history = FRAUD_SIM_METRICS.get_run_history()

        output = []
        output.append("# HELP fraud_sim_runs_total Total simulation runs created")
        output.append("# TYPE fraud_sim_runs_total counter")
        output.append(f"fraud_sim_runs_total {metrics['runs_total']}")

        output.append("# HELP fraud_sim_runs_in_progress Simulation runs currently executing")
        output.append("# TYPE fraud_sim_runs_in_progress gauge")
        output.append(f"fraud_sim_runs_in_progress {metrics['runs_in_progress']}")

        output.append("# HELP fraud_sim_runs_completed Successfully completed runs")
        output.append("# TYPE fraud_sim_runs_completed counter")
        output.append(f"fraud_sim_runs_completed {metrics['runs_completed']}")

        output.append("# HELP fraud_sim_runs_failed Failed runs")
        output.append("# TYPE fraud_sim_runs_failed counter")
        output.append(f"fraud_sim_runs_failed {metrics['runs_failed']}")

        output.append("# HELP fraud_sim_last_run_accuracy Accuracy of last completed run")
        output.append("# TYPE fraud_sim_last_run_accuracy gauge")
        output.append(f"fraud_sim_last_run_accuracy {metrics['last_run_accuracy']}")

        output.append("# HELP fraud_sim_last_run_precision Precision of last completed run")
        output.append("# TYPE fraud_sim_last_run_precision gauge")
        output.append(f"fraud_sim_last_run_precision {metrics['last_run_precision']}")

        output.append("# HELP fraud_sim_last_run_recall Recall of last completed run")
        output.append("# TYPE fraud_sim_last_run_recall gauge")
        output.append(f"fraud_sim_last_run_recall {metrics['last_run_recall']}")

        output.append("# HELP fraud_sim_last_run_f1_score F1 score of last completed run")
        output.append("# TYPE fraud_sim_last_run_f1_score gauge")
        output.append(f"fraud_sim_last_run_f1_score {metrics['last_run_f1_score']}")

        output.append("# HELP fraud_sim_total_transactions_analyzed Total transactions analyzed across all runs")
        output.append("# TYPE fraud_sim_total_transactions_analyzed counter")
        output.append(f"fraud_sim_total_transactions_analyzed {metrics['total_transactions_analyzed']}")

        output.append("# HELP fraud_sim_total_fraud_detected Total fraud detected across all runs")
        output.append("# TYPE fraud_sim_total_fraud_detected counter")
        output.append(f"fraud_sim_total_fraud_detected {metrics['total_fraud_detected']}")

        output.append("# HELP fraud_sim_pattern_flags Pattern flag detections")
        output.append("# TYPE fraud_sim_pattern_flags gauge")
        for flag, count in metrics['pattern_flags'].items():
            output.append(f'fraud_sim_pattern_flags{{flag="{flag}"}} {count}')

        # Per-run metrics for comparison charts
        output.append("# HELP fraud_sim_run_accuracy Per-run accuracy with run_id and fraud_type labels")
        output.append("# TYPE fraud_sim_run_accuracy gauge")
        for run in run_history:
            output.append(f'fraud_sim_run_accuracy{{run_id="{run["run_id"]}",fraud_type="{run["fraud_type"]}"}} {run["accuracy"]}')

        output.append("# HELP fraud_sim_run_precision Per-run precision with run_id and fraud_type labels")
        output.append("# TYPE fraud_sim_run_precision gauge")
        for run in run_history:
            output.append(f'fraud_sim_run_precision{{run_id="{run["run_id"]}",fraud_type="{run["fraud_type"]}"}} {run["precision"]}')

        output.append("# HELP fraud_sim_run_recall Per-run recall with run_id and fraud_type labels")
        output.append("# TYPE fraud_sim_run_recall gauge")
        for run in run_history:
            output.append(f'fraud_sim_run_recall{{run_id="{run["run_id"]}",fraud_type="{run["fraud_type"]}"}} {run["recall"]}')

        output.append("# HELP fraud_sim_run_f1_score Per-run F1 score with run_id and fraud_type labels")
        output.append("# TYPE fraud_sim_run_f1_score gauge")
        for run in run_history:
            output.append(f'fraud_sim_run_f1_score{{run_id="{run["run_id"]}",fraud_type="{run["fraud_type"]}"}} {run["f1_score"]}')

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4; charset=utf-8")
        self.end_headers()
        response = "\n".join(output) + "\n"
        self.wfile.write(response.encode('utf-8'))

    def send_json_response(self, data: Dict):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = json.dumps(data, indent=2)
        self.wfile.write(response.encode('utf-8'))

    def send_error_response(self, code: int, message: str):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        error_data = {"error": message, "timestamp": time.time()}
        response = json.dumps(error_data)
        self.wfile.write(response.encode('utf-8'))


def start_fraud_sim_server(port: int, output_dir: str = "./output/runs", kb_dir: str = "./kb"):
    """Start fraud simulation API server"""
    def run_server():
        try:
            run_manager = RunManager(output_dir=output_dir, kb_dir=kb_dir)
            server = HTTPServer(('0.0.0.0', port), FraudSimAPIHandler)
            server.run_manager = run_manager

            logging.getLogger(__name__).info(f"Fraud Simulation API server started on port {port}")
            server.serve_forever()
        except Exception as e:
            logging.getLogger(__name__).error(f"Fraud Simulation API server error: {e}")

    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    return thread
