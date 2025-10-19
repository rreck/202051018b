#!/usr/bin/env python3
"""
Run Management System
Manages fraud simulation runs with synthetic data generation and detection
"""

import json
import os
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, Optional, List

from synthetic_payment_generator import SyntheticPaymentGenerator
from card_testing_detector import CardTestingDetector


@dataclass
class RunConfig:
    """Configuration for a fraud simulation run"""
    run_id: str
    fraud_type: str
    transaction_count: int
    fraud_intensity: float
    detection_threshold: int
    timestamp: int


@dataclass
class RunMetrics:
    """Metrics collected during a run"""
    run_id: str
    fraud_type: str
    transaction_count: int
    fraud_count: int
    detected_count: int
    true_positives: int
    false_positives: int
    true_negatives: int
    false_negatives: int
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    score_distribution: Dict
    pattern_flag_counts: Dict
    processing_time: float
    status: str
    timestamp: int


class RunManager:
    """Manages fraud simulation runs"""

    def __init__(self, output_dir: str = "./output/runs", kb_dir: str = "./kb"):
        self.output_dir = output_dir
        self.kb_dir = kb_dir
        os.makedirs(output_dir, exist_ok=True)
        self.runs = {}  # run_id -> RunMetrics

    def create_run(self,
                   fraud_type: str = "card_testing",
                   transaction_count: int = 1000,
                   fraud_intensity: float = 0.10,
                   detection_threshold: int = 75) -> str:
        """
        Create and execute a new fraud simulation run

        Returns: run_id
        """
        # Generate run ID
        epoch = int(time.time())
        run_id = f"run_{fraud_type}_{epoch}"

        # Create run directory
        run_dir = os.path.join(self.output_dir, run_id)
        os.makedirs(run_dir, exist_ok=True)

        # Save run configuration
        config = RunConfig(
            run_id=run_id,
            fraud_type=fraud_type,
            transaction_count=transaction_count,
            fraud_intensity=fraud_intensity,
            detection_threshold=detection_threshold,
            timestamp=epoch
        )

        config_path = os.path.join(run_dir, "config.json")
        with open(config_path, 'w') as f:
            json.dump(asdict(config), f, indent=2)

        return run_id

    def execute_run(self, run_id: str) -> RunMetrics:
        """Execute a fraud simulation run"""
        run_dir = os.path.join(self.output_dir, run_id)

        # Load configuration
        config_path = os.path.join(run_dir, "config.json")
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        config = RunConfig(**config_data)

        start_time = time.time()

        # Step 1: Generate synthetic data
        generator = SyntheticPaymentGenerator(seed=config.timestamp)
        transactions = generator.generate_dataset(
            transaction_count=config.transaction_count,
            fraud_type=config.fraud_type,
            fraud_intensity=config.fraud_intensity
        )

        # Save to CSV
        csv_path = os.path.join(run_dir, "transactions.csv")
        generator.save_to_csv(transactions, csv_path)

        # Save ground truth
        ground_truth_path = os.path.join(run_dir, "ground_truth.json")
        generator.save_ground_truth(transactions, ground_truth_path)

        # Step 2: Run fraud detection
        detector = CardTestingDetector(threshold=config.detection_threshold)
        results = detector.analyze_batch(csv_path)

        # Save detection results
        results_path = os.path.join(run_dir, "detection_results.json")
        with open(results_path, 'w') as f:
            json.dump([r.to_dict() for r in results], f, indent=2)

        # Step 3: Calculate metrics
        confusion_matrix = detector.calculate_confusion_matrix(results, ground_truth_path)
        score_distribution = detector.get_score_distribution(results)
        pattern_flags = detector.get_pattern_flag_counts(results)

        processing_time = time.time() - start_time

        # Count fraud
        fraud_count = sum(1 for t in transactions if t.is_fraud)
        detected_count = sum(1 for r in results if r.fraud_detected)

        metrics = RunMetrics(
            run_id=run_id,
            fraud_type=config.fraud_type,
            transaction_count=config.transaction_count,
            fraud_count=fraud_count,
            detected_count=detected_count,
            true_positives=confusion_matrix['true_positives'],
            false_positives=confusion_matrix['false_positives'],
            true_negatives=confusion_matrix['true_negatives'],
            false_negatives=confusion_matrix['false_negatives'],
            accuracy=confusion_matrix['accuracy'],
            precision=confusion_matrix['precision'],
            recall=confusion_matrix['recall'],
            f1_score=confusion_matrix['f1_score'],
            score_distribution=score_distribution,
            pattern_flag_counts=pattern_flags,
            processing_time=processing_time,
            status="completed",
            timestamp=config.timestamp
        )

        # Save metrics
        metrics_path = os.path.join(run_dir, "metrics.json")
        with open(metrics_path, 'w') as f:
            json.dump(asdict(metrics), f, indent=2)

        # Store in memory
        self.runs[run_id] = metrics

        # Create pmem artifact
        self._create_pmem_artifact(metrics, run_dir)

        return metrics

    def _create_pmem_artifact(self, metrics: RunMetrics, run_dir: str):
        """Create pmem 1.0 artifact for run results"""
        epoch = metrics.timestamp
        artifact_path = os.path.join(self.kb_dir, "short", f"agent.fraud-sim.RESULT.{epoch}.md")

        # Create AICP header
        header = {
            "id": f"agent.fraud-sim.RESULT.{epoch}",
            "scope": "agent",
            "key": "RESULT",
            "epoch": epoch,
            "host_pid": f"{os.uname().nodename}_{os.getpid()}",
            "hash": "stub_hash",
            "cid": "stub_cid",
            "aicp": {
                "prov": {
                    "issuer": "did:agent:fraud-sim",
                    "issued": datetime.fromtimestamp(epoch).isoformat(),
                    "proof": "ed25519:stub"
                },
                "ucon": {
                    "constraints": ["synthetic-data-only", "test-environment"],
                    "obligations": ["track-detection-accuracy"]
                },
                "eval": {
                    "risk": "low",
                    "classification": "simulation",
                    "review_required": False
                }
            },
            "sources": [],
            "edges": [],
            "metrics": {
                "accuracy": metrics.accuracy,
                "precision": metrics.precision,
                "recall": metrics.recall,
                "f1_score": metrics.f1_score
            },
            "thresholds": {},
            "tags": [metrics.fraud_type, "simulation", f"run_{metrics.run_id}"],
            "sig": "stub_signature"
        }

        content = f"""```json
{json.dumps(header, indent=2)}
```

# Fraud Simulation Run: {metrics.run_id}

## Configuration
- **Fraud Type**: {metrics.fraud_type}
- **Transaction Count**: {metrics.transaction_count}
- **Fraud Intensity**: {(metrics.fraud_count / metrics.transaction_count * 100):.1f}%
- **Processing Time**: {metrics.processing_time:.2f}s

## Detection Results
- **True Positives**: {metrics.true_positives}
- **False Positives**: {metrics.false_positives}
- **True Negatives**: {metrics.true_negatives}
- **False Negatives**: {metrics.false_negatives}

## Performance Metrics
- **Accuracy**: {metrics.accuracy:.2%}
- **Precision**: {metrics.precision:.2%}
- **Recall**: {metrics.recall:.2%}
- **F1 Score**: {metrics.f1_score:.2%}

## Score Distribution
{json.dumps(metrics.score_distribution, indent=2)}

## Pattern Flags Detected
{json.dumps(metrics.pattern_flag_counts, indent=2)}

## Analysis
This run successfully demonstrated {metrics.fraud_type} detection capability with {metrics.accuracy:.1%} accuracy.
The system correctly identified {metrics.true_positives} of {metrics.fraud_count} fraudulent transactions.
"""

        os.makedirs(os.path.dirname(artifact_path), exist_ok=True)
        with open(artifact_path, 'w') as f:
            f.write(content)

    def get_run_metrics(self, run_id: str) -> Optional[RunMetrics]:
        """Retrieve metrics for a specific run"""
        if run_id in self.runs:
            return self.runs[run_id]

        # Try loading from disk
        run_dir = os.path.join(self.output_dir, run_id)
        metrics_path = os.path.join(run_dir, "metrics.json")

        if os.path.exists(metrics_path):
            with open(metrics_path, 'r') as f:
                metrics_data = json.load(f)
            metrics = RunMetrics(**metrics_data)
            self.runs[run_id] = metrics
            return metrics

        return None

    def list_runs(self) -> List[str]:
        """List all run IDs"""
        try:
            return [d for d in os.listdir(self.output_dir)
                    if os.path.isdir(os.path.join(self.output_dir, d)) and d.startswith('run_')]
        except FileNotFoundError:
            return []

    def get_all_metrics(self) -> List[RunMetrics]:
        """Get metrics for all runs"""
        run_ids = self.list_runs()
        metrics_list = []

        for run_id in run_ids:
            metrics = self.get_run_metrics(run_id)
            if metrics:
                metrics_list.append(metrics)

        return sorted(metrics_list, key=lambda m: m.timestamp, reverse=True)
