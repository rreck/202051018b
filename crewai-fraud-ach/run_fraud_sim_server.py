#!/usr/bin/env python3
"""
Standalone Fraud Simulation Metrics Server
Runs fraud_sim_api on port 8081 to expose metrics to Prometheus
"""

import sys
import os
import logging

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from fraud_sim_api import start_fraud_sim_server

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), "output/runs")
    kb_dir = os.path.join(os.path.dirname(__file__), "kb")

    # Use port 8082 (8080, 8081 are in use)
    port = 8082

    print(f"Starting Fraud Simulation API server on port {port}...")
    print(f"Metrics endpoint: http://localhost:{port}/sim/metrics")
    print(f"Status endpoint: http://localhost:{port}/sim/status")
    print(f"Create run: POST http://localhost:{port}/sim/run")

    thread = start_fraud_sim_server(port, output_dir=output_dir, kb_dir=kb_dir)

    try:
        # Keep main thread alive
        thread.join()
    except KeyboardInterrupt:
        print("\nShutting down...")
