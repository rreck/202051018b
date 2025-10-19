#!/usr/bin/env python3
"""
Benchmark suite for crewai-transcribe agent
Tests metrics collection under load
"""

import requests
import time
import json
from pathlib import Path
import subprocess
import sys

AGENT_API = "http://localhost:8083"
METRICS_URL = "http://localhost:9093/metrics"
PROMETHEUS_URL = "http://localhost:9095"

class TranscribeBenchmark:
    def __init__(self):
        self.results = {
            "start_time": time.time(),
            "tests": [],
            "metrics_snapshots": []
        }

    def log(self, msg):
        print(f"[{time.strftime('%H:%M:%S')}] {msg}")

    def get_metrics(self):
        """Fetch current metrics from agent"""
        try:
            resp = requests.get(METRICS_URL, timeout=5)
            return resp.text
        except Exception as e:
            self.log(f"ERROR fetching metrics: {e}")
            return None

    def parse_metric_value(self, metrics_text, metric_name):
        """Extract metric value from Prometheus format"""
        if not metrics_text:
            return None

        for line in metrics_text.split('\n'):
            if line.startswith(metric_name) and not line.startswith('#'):
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        return float(parts[-1])
                    except ValueError:
                        return None
        return None

    def check_health(self):
        """Verify agent is healthy"""
        self.log("Checking agent health...")
        try:
            resp = requests.get(f"{AGENT_API}/health", timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                self.log(f"✓ Agent healthy: {data.get('status')}")
                return True
            else:
                self.log(f"✗ Agent unhealthy: HTTP {resp.status_code}")
                return False
        except Exception as e:
            self.log(f"✗ Agent health check failed: {e}")
            return False

    def check_status(self):
        """Get detailed agent status"""
        self.log("Fetching agent status...")
        try:
            resp = requests.get(f"{AGENT_API}/status", timeout=5)
            if resp.status_code == 200:
                status = resp.json()
                self.log(f"✓ Model: {status.get('current_model')}")
                self.log(f"✓ Uptime: {status.get('uptime_seconds', 0):.0f}s")
                self.log(f"✓ Memory: {status.get('memory_usage_mb', 0):.0f} MB")
                self.log(f"✓ Jobs cached: {status.get('jobs_cached', 0)}")
                return status
            else:
                self.log(f"✗ Status fetch failed: HTTP {resp.status_code}")
                return None
        except Exception as e:
            self.log(f"✗ Status fetch failed: {e}")
            return None

    def snapshot_metrics(self, label):
        """Take snapshot of current metrics"""
        self.log(f"Snapshotting metrics: {label}")
        metrics_text = self.get_metrics()

        if not metrics_text:
            self.log("✗ Failed to get metrics")
            return None

        snapshot = {
            "timestamp": time.time(),
            "label": label,
            "metrics": {
                "files_processed": self.parse_metric_value(metrics_text, "transcribe_files_processed_total"),
                "files_failed": self.parse_metric_value(metrics_text, "transcribe_files_failed_total"),
                "files_skipped": self.parse_metric_value(metrics_text, "transcribe_files_skipped_total"),
            }
        }

        # Extract histogram data
        for line in metrics_text.split('\n'):
            if 'transcribe_processing_time_seconds' in line and not line.startswith('#'):
                snapshot["metrics"]["raw_line"] = line.strip()
                break

        self.results["metrics_snapshots"].append(snapshot)

        self.log(f"  Processed: {snapshot['metrics']['files_processed']}")
        self.log(f"  Failed: {snapshot['metrics']['files_failed']}")
        self.log(f"  Skipped: {snapshot['metrics']['files_skipped']}")

        return snapshot

    def test_batch_endpoint(self):
        """Test batch processing endpoint"""
        self.log("Testing /batch endpoint...")

        before = self.snapshot_metrics("before_batch")

        try:
            resp = requests.post(
                f"{AGENT_API}/batch",
                json={"input_pattern": "*.{wav,mp4,avi,mov}", "force": False},
                headers={"Content-Type": "application/json"},
                timeout=30
            )

            test_result = {
                "test": "batch_endpoint",
                "timestamp": time.time(),
                "status_code": resp.status_code,
                "success": resp.status_code == 200
            }

            if resp.status_code == 200:
                data = resp.json()
                test_result["response"] = data
                self.log(f"✓ Batch triggered: {json.dumps(data)}")
            else:
                self.log(f"✗ Batch failed: HTTP {resp.status_code}")
                test_result["error"] = resp.text

            self.results["tests"].append(test_result)

            # Wait for processing
            self.log("Waiting 5s for processing...")
            time.sleep(5)

            after = self.snapshot_metrics("after_batch")

            # Check if metrics changed
            if before and after:
                delta_processed = (after["metrics"]["files_processed"] or 0) - (before["metrics"]["files_processed"] or 0)
                delta_failed = (after["metrics"]["files_failed"] or 0) - (before["metrics"]["files_failed"] or 0)
                delta_skipped = (after["metrics"]["files_skipped"] or 0) - (before["metrics"]["files_skipped"] or 0)

                self.log(f"Metrics delta: +{delta_processed} processed, +{delta_failed} failed, +{delta_skipped} skipped")
                test_result["metrics_changed"] = (delta_processed + delta_failed + delta_skipped) > 0

            return test_result

        except Exception as e:
            self.log(f"✗ Batch test failed: {e}")
            test_result = {
                "test": "batch_endpoint",
                "timestamp": time.time(),
                "success": False,
                "error": str(e)
            }
            self.results["tests"].append(test_result)
            return test_result

    def check_prometheus_scraping(self):
        """Verify Prometheus is scraping the agent"""
        self.log("Checking Prometheus scraping...")

        try:
            # Query Prometheus for transcribe metrics
            query = "transcribe_files_processed_total"
            resp = requests.get(
                f"{PROMETHEUS_URL}/api/v1/query",
                params={"query": query},
                timeout=10
            )

            if resp.status_code == 200:
                data = resp.json()
                if data.get("status") == "success":
                    results = data.get("data", {}).get("result", [])
                    if results:
                        self.log(f"✓ Prometheus has {len(results)} series for {query}")
                        for result in results:
                            value = result.get("value", [None, None])[1]
                            self.log(f"  Value: {value}")
                        return True
                    else:
                        self.log(f"✗ Prometheus has NO data for {query}")
                        return False
                else:
                    self.log(f"✗ Prometheus query failed: {data.get('error')}")
                    return False
            else:
                self.log(f"✗ Prometheus API error: HTTP {resp.status_code}")
                return False

        except Exception as e:
            self.log(f"✗ Prometheus check failed: {e}")
            return False

    def continuous_load_test(self, duration_seconds=30):
        """Run continuous load for specified duration"""
        self.log(f"Starting {duration_seconds}s continuous load test...")

        start = time.time()
        iterations = 0

        self.snapshot_metrics(f"load_start")

        while (time.time() - start) < duration_seconds:
            iterations += 1
            self.log(f"Load iteration {iterations}...")

            try:
                # Trigger batch
                resp = requests.post(
                    f"{AGENT_API}/batch",
                    json={"input_pattern": "*.{wav,mp4,avi,mov}", "force": False},
                    headers={"Content-Type": "application/json"},
                    timeout=15
                )
                if resp.status_code == 200:
                    self.log(f"  ✓ Batch {iterations} triggered")
                else:
                    self.log(f"  ✗ Batch {iterations} failed: HTTP {resp.status_code}")

                # Check status
                requests.get(f"{AGENT_API}/status", timeout=5)

                # Brief pause
                time.sleep(2)

            except Exception as e:
                self.log(f"  ✗ Load iteration {iterations} error: {e}")

        self.snapshot_metrics(f"load_end")

        elapsed = time.time() - start
        self.log(f"Load test complete: {iterations} iterations in {elapsed:.1f}s")

        return {
            "test": "continuous_load",
            "duration_seconds": elapsed,
            "iterations": iterations,
            "success": True
        }

    def run_full_benchmark(self):
        """Run complete benchmark suite"""
        self.log("=" * 60)
        self.log("CREWAI-TRANSCRIBE BENCHMARK")
        self.log("=" * 60)

        # Phase 1: Health checks
        if not self.check_health():
            self.log("FATAL: Agent not healthy, aborting")
            return False

        status = self.check_status()
        if not status:
            self.log("FATAL: Cannot get agent status, aborting")
            return False

        # Phase 2: Initial metrics
        self.snapshot_metrics("initial")

        # Phase 3: Batch test
        self.test_batch_endpoint()

        # Phase 4: Continuous load
        load_result = self.continuous_load_test(duration_seconds=30)
        self.results["tests"].append(load_result)

        # Phase 5: Final metrics
        time.sleep(3)
        self.snapshot_metrics("final")

        # Phase 6: Verify Prometheus
        prom_ok = self.check_prometheus_scraping()

        # Summary
        self.log("=" * 60)
        self.log("BENCHMARK SUMMARY")
        self.log("=" * 60)

        total_time = time.time() - self.results["start_time"]
        self.log(f"Total duration: {total_time:.1f}s")
        self.log(f"Tests run: {len(self.results['tests'])}")
        self.log(f"Metric snapshots: {len(self.results['metrics_snapshots'])}")

        if len(self.results["metrics_snapshots"]) >= 2:
            first = self.results["metrics_snapshots"][0]
            last = self.results["metrics_snapshots"][-1]

            delta_processed = (last["metrics"]["files_processed"] or 0) - (first["metrics"]["files_processed"] or 0)
            delta_failed = (last["metrics"]["files_failed"] or 0) - (first["metrics"]["files_failed"] or 0)

            self.log(f"Files processed during benchmark: {delta_processed}")
            self.log(f"Files failed during benchmark: {delta_failed}")

        self.log(f"Prometheus scraping: {'✓ YES' if prom_ok else '✗ NO'}")

        # Save results
        results_file = "benchmark_results.json"
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        self.log(f"Results saved to {results_file}")

        self.log("=" * 60)

        return prom_ok


def main():
    benchmark = TranscribeBenchmark()
    success = benchmark.run_full_benchmark()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
