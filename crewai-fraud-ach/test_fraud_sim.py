#!/usr/bin/env python3
"""
Test script for fraud simulation system
"""

import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from run_manager import RunManager


def test_card_testing_simulation():
    """Test card testing fraud simulation"""
    print("=" * 80)
    print("Card Testing Fraud Simulation Test")
    print("=" * 80)

    # Initialize run manager
    output_dir = "./output/runs"
    kb_dir = "./kb"
    run_manager = RunManager(output_dir=output_dir, kb_dir=kb_dir)

    # Create run
    print("\n1. Creating run...")
    run_id = run_manager.create_run(
        fraud_type="card_testing",
        transaction_count=500,
        fraud_intensity=0.15,  # 15% fraud
        detection_threshold=75
    )
    print(f"   Run ID: {run_id}")

    # Execute run
    print("\n2. Executing run...")
    metrics = run_manager.execute_run(run_id)

    # Display results
    print("\n3. Results:")
    print(f"   Transaction Count: {metrics.transaction_count}")
    print(f"   Fraud Count: {metrics.fraud_count}")
    print(f"   Detected Count: {metrics.detected_count}")
    print(f"\n   Confusion Matrix:")
    print(f"   - True Positives:  {metrics.true_positives}")
    print(f"   - False Positives: {metrics.false_positives}")
    print(f"   - True Negatives:  {metrics.true_negatives}")
    print(f"   - False Negatives: {metrics.false_negatives}")
    print(f"\n   Performance Metrics:")
    print(f"   - Accuracy:  {metrics.accuracy:.2%}")
    print(f"   - Precision: {metrics.precision:.2%}")
    print(f"   - Recall:    {metrics.recall:.2%}")
    print(f"   - F1 Score:  {metrics.f1_score:.2%}")
    print(f"\n   Score Distribution:")
    for range_name, count in metrics.score_distribution.items():
        print(f"   - {range_name}: {count}")
    print(f"\n   Pattern Flags:")
    for flag, count in metrics.pattern_flag_counts.items():
        print(f"   - {flag}: {count}")
    print(f"\n   Processing Time: {metrics.processing_time:.2f}s")

    # Verify output files
    run_dir = os.path.join(output_dir, run_id)
    print(f"\n4. Output files in {run_dir}:")
    for filename in sorted(os.listdir(run_dir)):
        filepath = os.path.join(run_dir, filename)
        size = os.path.getsize(filepath)
        print(f"   - {filename} ({size:,} bytes)")

    # Verify pmem artifact
    import time
    epoch = metrics.timestamp
    pmem_path = os.path.join(kb_dir, "short", f"agent.fraud-sim.RESULT.{epoch}.md")
    if os.path.exists(pmem_path):
        print(f"\n5. PMEM artifact created: {pmem_path}")
    else:
        print(f"\n5. WARNING: PMEM artifact not found at {pmem_path}")

    print("\n" + "=" * 80)
    print("Test completed successfully!")
    print("=" * 80)

    return metrics


if __name__ == "__main__":
    test_card_testing_simulation()
