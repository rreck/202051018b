#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright (c) RRECKTEK LLC
# Project: CrewAI Fraud Detection Agent - ACH Fraud Detection
# Version: 1.0.0
# Built: @EPOCH
#
# Purpose:
#   ACH fraud detection agent that analyzes ACH/NACHA transaction files,
#   detects fraud patterns, generates synthetic ACH data with fraud scenarios,
#   and maintains biomimicry-driven persistent memory for emergent learning.
#
# Features:
#   - ACH/NACHA file parsing and validation
#   - Multi-strategy fraud detection (velocity, duplicates, anomalies, routing)
#   - Synthetic ACH data generation with labeled fraud patterns
#   - Biomimicry memory system with provenance and edge tracking
#   - Agent-to-Agent (A2A) HTTP API
#   - Prometheus metrics and Grafana dashboard registration
#   - Daemon mode and watch mode support
#
# Exit codes:
#   0 = success / no work needed
#   1 = general error
#   2 = at least one detection failed
#   3 = daemon startup failed
# -----------------------------------------------------------------------------

import argparse
import atexit
import daemon
import daemon.pidfile
import json
import logging
import logging.handlers
import os
import random
import signal
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse, parse_qs
import requests

# Import our modules
from ach_schema import (
    ACHFile, ACHBatch, EntryDetailRecord, AddendaRecord, ACHParser,
    TransactionCode, ServiceClassCode, StandardEntryClassCode,
    generate_routing_number, validate_routing_number
)
from fraud_engine import (
    FraudDetectionEngine, FraudDetectionConfig, TransactionRecord,
    FraudType
)
from memory_system import (
    MemoryStore, MemoryArtifact, MemoryScope, MemoryKey, MemoryEdge
)

# ---- Defaults ----------------------------------------------------------------

DEFAULT_INPUT = os.environ.get("INPUT_DIR", "./input")
DEFAULT_OUTPUT = os.environ.get("OUTPUT_DIR", "./output")
DEFAULT_KB_DIR = os.environ.get("KB_DIR", "./kb")
DEFAULT_PIDFILE = os.environ.get("PIDFILE", "/var/run/fraud-ach-agent.pid")
DEFAULT_METRICS_PORT = int(os.environ.get("METRICS_PORT", "9090"))
DEFAULT_API_PORT = int(os.environ.get("API_PORT", "8080"))
DEFAULT_SYNTHETIC_TRANSACTION_COUNT = 100

# ---- Global metrics and state -----------------------------------------------

class AgentMetrics:
    """Thread-safe metrics collection for Prometheus export"""
    def __init__(self):
        self._lock = threading.Lock()
        self._metrics = {
            'files_processed_total': 0,
            'files_failed_total': 0,
            'files_skipped_total': 0,
            'transactions_analyzed_total': 0,
            'fraud_detected_total': 0,
            'fraud_by_type': {ft: 0 for ft in FraudType.ALL_TYPES},
            'processing_time_seconds_total': 0.0,
            'queue_depth': 0,
            'daemon_uptime_seconds': 0,
            'last_processing_timestamp': 0,
            'active_jobs': 0,
            'memory_artifacts_total': 0,
            'memory_edges_total': 0,
            'cluster_formation_total': 0,
            'synthetic_files_generated_total': 0,
            'synthetic_transactions_generated_total': 0,
        }
        self._start_time = time.time()

    def increment(self, metric: str, value: float = 1.0):
        with self._lock:
            if metric in self._metrics:
                self._metrics[metric] += value
            elif '.' in metric:
                # Handle nested metrics like fraud_by_type.velocity_attack
                parts = metric.split('.')
                if parts[0] in self._metrics and isinstance(self._metrics[parts[0]], dict):
                    if parts[1] in self._metrics[parts[0]]:
                        self._metrics[parts[0]][parts[1]] += value

    def set_gauge(self, metric: str, value: float):
        with self._lock:
            self._metrics[metric] = value

    def get_metrics(self) -> Dict:
        with self._lock:
            metrics = self._metrics.copy()
            metrics['daemon_uptime_seconds'] = time.time() - self._start_time
            return metrics

METRICS = AgentMetrics()
SHUTDOWN_EVENT = threading.Event()

# ---- Logging setup -----------------------------------------------------------

def setup_logging(daemon_mode: bool = False, log_level: str = "INFO"):
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level.upper()))
    logger.handlers.clear()

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    try:
        file_handler = logging.FileHandler('/var/log/fraud-ach-agent.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (PermissionError, FileNotFoundError):
        file_handler = logging.FileHandler('./fraud-ach-agent.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if daemon_mode:
        try:
            syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
            syslog_formatter = logging.Formatter('fraud-ach-agent: %(levelname)s - %(message)s')
            syslog_handler.setFormatter(syslog_formatter)
            logger.addHandler(syslog_handler)
        except Exception as e:
            logger.warning(f"Could not setup syslog handler: {e}")
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# ---- Utilities ---------------------------------------------------------------

def epoch() -> int:
    return int(time.time())

def ensure_directories(*paths) -> bool:
    logger = logging.getLogger(__name__)
    success = True

    for path in paths:
        try:
            os.makedirs(path, exist_ok=True)
            test_file = os.path.join(path, '.write_test')
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            logger.info(f"Directory verified: {path}")
        except Exception as e:
            logger.error(f"Error with directory {path}: {e}")
            success = False

    return success

def log_append(logf: str, text: str):
    try:
        with open(logf, "a", encoding="utf-8") as f:
            f.write(text)
            if not text.endswith("\n"):
                f.write("\n")
    except Exception as e:
        logging.getLogger(__name__).error(f"Error writing to log file {logf}: {e}")

# ---- Synthetic ACH Data Generation -------------------------------------------

class SyntheticACHGenerator:
    """Generate synthetic ACH files with fraud patterns"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.fake_names = [
            "Alice Johnson", "Bob Smith", "Carol Davis", "David Wilson", "Eva Brown",
            "Frank Miller", "Grace Taylor", "Henry Anderson", "Ivy Thomas", "Jack Jackson",
            "Karen White", "Larry Martinez", "Mary Garcia", "Nathan Lee", "Olivia Martinez"
        ]
        self.fake_companies = [
            "ACME CORP", "GLOBEX INC", "INITECH LLC", "UMBRELLA CO", "WAYNE ENTERPRISES"
        ]

    def generate_synthetic_ach_file(self,
                                     transaction_count: int = 100,
                                     fraud_ratio: float = 0.05) -> Tuple[ACHFile, List[Dict]]:
        """
        Generate synthetic ACH file with fraud patterns.
        Returns (ACHFile, fraud_labels)
        """
        ach_file = ACHFile(
            immediate_destination='091000019',
            immediate_origin='091000019',
            immediate_destination_name='RECEIVING BANK',
            immediate_origin_name='ORIGINATING BANK'
        )

        batch = ACHBatch(
            service_class_code=ServiceClassCode.MIXED,
            company_name=random.choice(self.fake_companies),
            company_id='1234567890',
            sec_code=StandardEntryClassCode.PPD,
            company_entry_description='PAYROLL',
            originating_dfi_id='12345678',
            batch_number=1
        )

        fraud_labels = []
        fraud_count = int(transaction_count * fraud_ratio)
        fraud_indices = set(random.sample(range(transaction_count), fraud_count))

        # Generate transactions
        for i in range(transaction_count):
            is_fraud = i in fraud_indices

            if is_fraud:
                entry, label = self._generate_fraud_transaction(i)
            else:
                entry, label = self._generate_legitimate_transaction(i)

            batch.add_entry(entry)
            fraud_labels.append(label)

        ach_file.add_batch(batch)

        return ach_file, fraud_labels

    def _generate_legitimate_transaction(self, seq: int) -> Tuple[EntryDetailRecord, Dict]:
        """Generate a legitimate transaction"""
        amount = random.randint(50000, 500000)  # $500 to $5000

        entry = EntryDetailRecord(
            transaction_code=random.choice([TransactionCode.CHECKING_CREDIT, TransactionCode.SAVINGS_CREDIT]),
            receiving_dfi_routing=generate_routing_number(valid=True),
            receiving_dfi_account=str(random.randint(100000000, 999999999)),
            amount=amount,
            individual_id=f"EMP{random.randint(1000, 9999)}",
            individual_name=random.choice(self.fake_names),
            discretionary_data='',
            addenda_indicator='0'
        )

        label = {
            'transaction_id': entry.trace_number,
            'fraud_type': FraudType.LEGITIMATE,
            'fraud_score': 0,
            'amount': amount
        }

        return entry, label

    def _generate_fraud_transaction(self, seq: int) -> Tuple[EntryDetailRecord, Dict]:
        """Generate a fraudulent transaction with specific pattern"""
        fraud_type = random.choice([
            FraudType.INVALID_ROUTING,
            FraudType.ROUND_AMOUNT_PATTERN,
            FraudType.AMOUNT_ANOMALY
        ])

        if fraud_type == FraudType.INVALID_ROUTING:
            # Invalid routing number
            entry = EntryDetailRecord(
                transaction_code=TransactionCode.CHECKING_DEBIT,
                receiving_dfi_routing=generate_routing_number(valid=False),
                receiving_dfi_account=str(random.randint(100000000, 999999999)),
                amount=random.randint(100000, 500000),
                individual_id=f"FRAUD{seq}",
                individual_name=random.choice(self.fake_names),
                discretionary_data='',
                addenda_indicator='0'
            )
            fraud_score = 95

        elif fraud_type == FraudType.ROUND_AMOUNT_PATTERN:
            # Suspiciously round amount
            round_amounts = [100000, 50000, 250000, 500000, 1000000]  # $1k, $500, $2.5k, $5k, $10k
            entry = EntryDetailRecord(
                transaction_code=TransactionCode.CHECKING_DEBIT,
                receiving_dfi_routing=generate_routing_number(valid=True),
                receiving_dfi_account=str(random.randint(100000000, 999999999)),
                amount=random.choice(round_amounts),
                individual_id=f"SUSP{seq}",
                individual_name=random.choice(self.fake_names),
                discretionary_data='',
                addenda_indicator='0'
            )
            fraud_score = 40

        else:  # AMOUNT_ANOMALY
            # Unusually high amount
            entry = EntryDetailRecord(
                transaction_code=TransactionCode.CHECKING_DEBIT,
                receiving_dfi_routing=generate_routing_number(valid=True),
                receiving_dfi_account=str(random.randint(100000000, 999999999)),
                amount=random.randint(5000000, 10000000),  # $50k to $100k
                individual_id=f"ANOM{seq}",
                individual_name=random.choice(self.fake_names),
                discretionary_data='',
                addenda_indicator='0'
            )
            fraud_score = 70

        label = {
            'transaction_id': entry.trace_number,
            'fraud_type': fraud_type,
            'fraud_score': fraud_score,
            'amount': entry.amount
        }

        return entry, label

# ---- Core processing ---------------------------------------------------------

def process_ach_file(
    input_path: str,
    output_dir: str,
    kb_dir: str,
    fraud_engine: FraudDetectionEngine,
    memory_store: MemoryStore,
    force: bool = False
) -> Tuple[str, Optional[str], str]:
    """
    Process an ACH file for fraud detection.
    Returns (status, output_path_or_None, log_path):
      status in {"OK", "FAIL", "SKIP"}
    """
    logger = logging.getLogger(__name__)
    METRICS.increment('active_jobs')

    try:
        filename = os.path.basename(input_path)
        logs_dir = os.path.join(output_dir, "logs")
        os.makedirs(logs_dir, exist_ok=True)

        logf = os.path.join(logs_dir, f"{epoch()}.{filename}.log")
        logger.info(f"Processing {input_path}")
        log_append(logf, f"Processing {input_path} at {datetime.now()}")

        start_time = time.time()

        # Parse ACH file
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        parsed = ACHParser.parse_file(content)

        if parsed['errors']:
            log_append(logf, f"Parse errors: {parsed['errors']}")
            METRICS.increment('files_failed_total')
            return ("FAIL", None, logf)

        # Analyze transactions
        fraud_results = []
        transaction_count = 0

        for batch in parsed['batches']:
            for entry_data in batch['entries']:
                entry = entry_data['entry']
                transaction_count += 1

                # Create transaction record
                transaction = TransactionRecord(
                    transaction_id=entry['trace_number'],
                    timestamp=epoch(),
                    routing_number=entry['receiving_dfi_routing'],
                    account_number=entry['receiving_dfi_account'],
                    amount=entry['amount'],
                    transaction_code=entry['transaction_code'],
                    individual_name=entry['individual_name'],
                    individual_id=entry['individual_id'],
                    trace_number=entry['trace_number']
                )

                # Analyze for fraud
                result = fraud_engine.analyze_transaction(transaction)
                fraud_results.append(result.to_dict())

                if result.fraud_detected:
                    METRICS.increment('fraud_detected_total')
                    for fraud_type in result.fraud_types:
                        METRICS.increment(f'fraud_by_type.{fraud_type}')

                    # Create memory artifact for fraud detection
                    memory_artifact = MemoryArtifact(
                        scope=MemoryScope.AGENT,
                        key=MemoryKey.RESULT,
                        agent_name='fraud-ach',
                        content=f"Fraud detected: {fraud_type} (score: {result.risk_score})\nTransaction: {transaction.trace_number}\nDetails: {result.details}",
                        tags=['fraud', fraud_type, f'risk_{result.risk_level}']
                    )
                    memory_store.save_artifact(memory_artifact)
                    METRICS.increment('memory_artifacts_total')

        METRICS.increment('transactions_analyzed_total', transaction_count)

        # Write fraud analysis results
        output_path = os.path.join(output_dir, f"{epoch()}.{filename}.fraud-analysis.json")

        analysis_output = {
            'file': input_path,
            'analyzed_at': datetime.now().isoformat(),
            'transaction_count': transaction_count,
            'fraud_detected_count': sum(1 for r in fraud_results if r['fraud_detected']),
            'fraud_results': fraud_results,
            'engine_statistics': fraud_engine.get_statistics()
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_output, f, indent=2)

        processing_time = time.time() - start_time
        METRICS.increment('processing_time_seconds_total', processing_time)
        METRICS.increment('files_processed_total')
        METRICS.set_gauge('last_processing_timestamp', time.time())

        log_append(logf, f"SUCCESS: Analyzed {transaction_count} transactions in {processing_time:.2f}s")
        log_append(logf, f"Output: {output_path}")

        logger.info(f"Successfully processed {input_path}")
        return ("OK", output_path, logf)

    except Exception as e:
        logger.error(f"Error processing {input_path}: {e}")
        log_append(logf, f"ERROR: {e}")
        METRICS.increment('files_failed_total')
        return ("FAIL", None, logf)

    finally:
        METRICS.increment('active_jobs', -1)

def generate_synthetic_ach_file(
    output_dir: str,
    transaction_count: int = DEFAULT_SYNTHETIC_TRANSACTION_COUNT,
    fraud_ratio: float = 0.05
) -> Tuple[str, Optional[str], str]:
    """Generate synthetic ACH file with fraud patterns"""
    logger = logging.getLogger(__name__)
    METRICS.increment('active_jobs')

    try:
        logs_dir = os.path.join(output_dir, "logs")
        os.makedirs(logs_dir, exist_ok=True)

        logf = os.path.join(logs_dir, f"{epoch()}.synthetic.log")
        log_append(logf, f"Generating synthetic ACH file at {datetime.now()}")

        start_time = time.time()

        generator = SyntheticACHGenerator()
        ach_file, fraud_labels = generator.generate_synthetic_ach_file(
            transaction_count=transaction_count,
            fraud_ratio=fraud_ratio
        )

        # Write ACH file
        ach_output_path = os.path.join(output_dir, f"{epoch()}.synthetic.ach")
        with open(ach_output_path, 'w', encoding='utf-8') as f:
            f.write(ach_file.to_nacha())

        # Write labels
        labels_output_path = os.path.join(output_dir, f"{epoch()}.synthetic.labels.json")
        with open(labels_output_path, 'w', encoding='utf-8') as f:
            json.dump({
                'generated_at': datetime.now().isoformat(),
                'transaction_count': transaction_count,
                'fraud_ratio': fraud_ratio,
                'labels': fraud_labels
            }, f, indent=2)

        processing_time = time.time() - start_time
        METRICS.increment('synthetic_files_generated_total')
        METRICS.increment('synthetic_transactions_generated_total', transaction_count)

        log_append(logf, f"SUCCESS: Generated {transaction_count} transactions in {processing_time:.2f}s")
        log_append(logf, f"ACH File: {ach_output_path}")
        log_append(logf, f"Labels: {labels_output_path}")

        logger.info(f"Successfully generated synthetic ACH file: {ach_output_path}")
        return ("OK", ach_output_path, logf)

    except Exception as e:
        logger.error(f"Error generating synthetic ACH file: {e}")
        log_append(logf, f"ERROR: {e}")
        return ("FAIL", None, logf)

    finally:
        METRICS.increment('active_jobs', -1)

# ---- Batch processing and daemon modes ---------------------------------------

def list_ach_files(input_dir: str) -> List[str]:
    """List all ACH files in input directory"""
    try:
        files = []
        for f in os.listdir(input_dir):
            if f.endswith('.ach') or f.endswith('.txt'):
                files.append(os.path.join(input_dir, f))
        files.sort()
        return files
    except FileNotFoundError:
        logging.getLogger(__name__).warning(f"Input directory not found: {input_dir}")
        return []
    except Exception as e:
        logging.getLogger(__name__).error(f"Error listing ACH files: {e}")
        return []

def batch(input_dir: str, output_dir: str, kb_dir: str, force: bool,
          fraud_engine: FraudDetectionEngine, memory_store: MemoryStore) -> int:
    """Process all ACH files in input directory"""
    logger = logging.getLogger(__name__)
    files = list_ach_files(input_dir)

    if not files:
        logger.info("No ACH files found in input/")
        return 0

    METRICS.set_gauge('queue_depth', len(files))
    summary = {"OK": 0, "FAIL": 0, "SKIP": 0}

    with ThreadPoolExecutor(max_workers=min(4, len(files))) as executor:
        futures = []
        for file_path in files:
            future = executor.submit(
                process_ach_file, file_path, output_dir, kb_dir,
                fraud_engine, memory_store, force
            )
            futures.append((file_path, future))

        for file_path, future in futures:
            try:
                status, output_path, log_path = future.result(timeout=300)
                summary[status] += 1
                print(f"{status}\t{file_path}\t{output_path or ''}\t{log_path}")
                logger.info(f"Batch result: {status} for {file_path}")
            except Exception as e:
                summary["FAIL"] += 1
                logger.error(f"Batch processing error for {file_path}: {e}")
                print(f"FAIL\t{file_path}\t\terror")

    METRICS.set_gauge('queue_depth', 0)
    logger.info(f"Batch complete: {summary}")
    return 0 if summary["FAIL"] == 0 else 2

def watch(input_dir: str, output_dir: str, kb_dir: str, sleep_sec: int, force: bool,
          fraud_engine: FraudDetectionEngine, memory_store: MemoryStore):
    """Watch mode - continuously monitor input directory"""
    logger = logging.getLogger(__name__)
    logger.info(f"[watch] scanning every {sleep_sec}s — Ctrl-C to stop")

    while not SHUTDOWN_EVENT.is_set():
        try:
            batch(input_dir, output_dir, kb_dir, force, fraud_engine, memory_store)

            # Decay memory edges periodically
            memory_store.decay_edges()

            for _ in range(max(1, sleep_sec)):
                if SHUTDOWN_EVENT.is_set():
                    break
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Watch mode interrupted by user")
            break
        except Exception as e:
            logger.error(f"Error in watch loop: {e}")
            time.sleep(5)

def daemon_main(input_dir: str, output_dir: str, kb_dir: str, sleep_sec: int, force: bool):
    """Main daemon loop"""
    logger = logging.getLogger(__name__)
    logger.info("Daemon mode started")

    def signal_handler(signum, frame):
        logger.info(f"Received signal {signum}, shutting down...")
        SHUTDOWN_EVENT.set()

    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # Initialize fraud engine and memory store
    fraud_engine = FraudDetectionEngine()
    memory_store = MemoryStore(base_dir=kb_dir)

    try:
        watch(input_dir, output_dir, kb_dir, sleep_sec, force, fraud_engine, memory_store)
    except Exception as e:
        logger.error(f"Daemon error: {e}")
        return 1

    logger.info("Daemon shutdown complete")
    return 0

# ---- Prometheus metrics server -----------------------------------------------

class MetricsHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress HTTP logs

    def do_GET(self):
        if self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4; charset=utf-8")
            self.end_headers()

            metrics = METRICS.get_metrics()

            output = []
            output.append("# HELP fraud_ach_files_processed_total Total ACH files processed")
            output.append("# TYPE fraud_ach_files_processed_total counter")
            output.append(f"fraud_ach_files_processed_total {metrics['files_processed_total']}")

            output.append("# HELP fraud_ach_files_failed_total Total ACH files that failed")
            output.append("# TYPE fraud_ach_files_failed_total counter")
            output.append(f"fraud_ach_files_failed_total {metrics['files_failed_total']}")

            output.append("# HELP fraud_ach_transactions_analyzed_total Total transactions analyzed")
            output.append("# TYPE fraud_ach_transactions_analyzed_total counter")
            output.append(f"fraud_ach_transactions_analyzed_total {metrics['transactions_analyzed_total']}")

            output.append("# HELP fraud_ach_fraud_detected_total Total fraud instances detected")
            output.append("# TYPE fraud_ach_fraud_detected_total counter")
            output.append(f"fraud_ach_fraud_detected_total {metrics['fraud_detected_total']}")

            output.append("# HELP fraud_ach_fraud_by_type Fraud detections by type")
            output.append("# TYPE fraud_ach_fraud_by_type counter")
            for fraud_type, count in metrics['fraud_by_type'].items():
                output.append(f'fraud_ach_fraud_by_type{{type="{fraud_type}"}} {count}')

            output.append("# HELP fraud_ach_memory_artifacts_total Total memory artifacts created")
            output.append("# TYPE fraud_ach_memory_artifacts_total counter")
            output.append(f"fraud_ach_memory_artifacts_total {metrics['memory_artifacts_total']}")

            output.append("# HELP fraud_ach_daemon_uptime_seconds Agent uptime")
            output.append("# TYPE fraud_ach_daemon_uptime_seconds gauge")
            output.append(f"fraud_ach_daemon_uptime_seconds {metrics['daemon_uptime_seconds']:.2f}")

            response = "\n".join(output) + "\n"
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def start_metrics_server(port: int):
    def run_server():
        try:
            server = HTTPServer(('0.0.0.0', port), MetricsHandler)
            logging.getLogger(__name__).info(f"Metrics server started on port {port}")
            server.serve_forever()
        except Exception as e:
            logging.getLogger(__name__).error(f"Metrics server error: {e}")

    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    return thread

# ---- A2A API server ----------------------------------------------------------

class A2AHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress HTTP logs

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == "/status":
            self.send_json_response({
                "status": "running",
                "metrics": METRICS.get_metrics(),
                "timestamp": time.time()
            })
        elif path == "/health":
            self.send_json_response({"status": "healthy"})
        elif path == "/config":
            config = {
                "input_dir": getattr(self.server, 'input_dir', 'unknown'),
                "output_dir": getattr(self.server, 'output_dir', 'unknown'),
                "kb_dir": getattr(self.server, 'kb_dir', 'unknown')
            }
            self.send_json_response(config)
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

        if path == "/job":
            result = self.handle_job_request(data)
            self.send_json_response(result)
        elif path == "/batch":
            result = self.handle_batch_request(data)
            self.send_json_response(result)
        else:
            self.send_error_response(404, "Endpoint not found")

    def handle_job_request(self, data: dict) -> dict:
        # Implementation would go here
        return {"status": "processing", "timestamp": time.time()}

    def handle_batch_request(self, data: dict) -> dict:
        # Implementation would go here
        return {"status": "batch_started", "timestamp": time.time()}

    def send_json_response(self, data: dict):
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

def start_a2a_server(port: int, **server_config):
    def run_server():
        try:
            server = HTTPServer(('0.0.0.0', port), A2AHandler)
            for key, value in server_config.items():
                setattr(server, key, value)

            logging.getLogger(__name__).info(f"A2A API server started on port {port}")
            server.serve_forever()
        except Exception as e:
            logging.getLogger(__name__).error(f"A2A API server error: {e}")

    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    return thread

# ---- Main entry point --------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="CrewAI Fraud Detection Agent - ACH Fraud Detection",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    ap.add_argument("-i", "--input", default=DEFAULT_INPUT, help="input directory")
    ap.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="output directory")
    ap.add_argument("-k", "--kb", default=DEFAULT_KB_DIR, help="knowledge base directory")
    ap.add_argument("-w", "--watch", action="store_true", help="watch mode")
    ap.add_argument("--daemon", action="store_true", help="daemon mode")
    ap.add_argument("-s", "--sleep", type=int, default=10, help="scan interval seconds")
    ap.add_argument("-f", "--force", action="store_true", help="force reprocessing")
    ap.add_argument("--generate", action="store_true", help="generate synthetic ACH file")
    ap.add_argument("--transactions", type=int, default=DEFAULT_SYNTHETIC_TRANSACTION_COUNT,
                   help="transactions to generate")
    ap.add_argument("--fraud-ratio", type=float, default=0.05, help="fraud ratio (0.0-1.0)")
    ap.add_argument("--pidfile", default=DEFAULT_PIDFILE, help="PID file path")
    ap.add_argument("--metrics-port", type=int, default=DEFAULT_METRICS_PORT, help="metrics port")
    ap.add_argument("--api-port", type=int, default=DEFAULT_API_PORT, help="API port")
    ap.add_argument("--log-level", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], default='INFO')

    args = ap.parse_args()

    if args.watch and args.daemon:
        print("ERROR: Cannot use both --watch and --daemon", file=sys.stderr)
        return 1

    setup_logging(daemon_mode=args.daemon, log_level=args.log_level)
    logger = logging.getLogger(__name__)

    if not ensure_directories(args.input, args.output, args.kb,
                             os.path.join(args.output, "logs"),
                             os.path.join(args.kb, "short"),
                             os.path.join(args.kb, "long")):
        logger.error("Failed to create required directories")
        return 2

    logger.info(f"Starting metrics server on port {args.metrics_port}")
    start_metrics_server(args.metrics_port)

    logger.info(f"Starting A2A API server on port {args.api_port}")
    start_a2a_server(
        args.api_port,
        input_dir=args.input,
        output_dir=args.output,
        kb_dir=args.kb
    )

    try:
        if args.generate:
            # Generate synthetic ACH file
            status, output_path, log_path = generate_synthetic_ach_file(
                args.output, args.transactions, args.fraud_ratio
            )
            print(f"{status}\t{output_path}\t{log_path}")
            return 0 if status == "OK" else 1

        elif args.daemon:
            return daemon_main(args.input, args.output, args.kb, args.sleep, args.force)

        elif args.watch:
            fraud_engine = FraudDetectionEngine()
            memory_store = MemoryStore(base_dir=args.kb)
            watch(args.input, args.output, args.kb, args.sleep, args.force,
                 fraud_engine, memory_store)
            return 0

        else:
            fraud_engine = FraudDetectionEngine()
            memory_store = MemoryStore(base_dir=args.kb)
            return batch(args.input, args.output, args.kb, args.force,
                        fraud_engine, memory_store)

    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        return 0
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
