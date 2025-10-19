# Fraud Simulation System - Complete Setup Documentation

## Infrastructure Status

### Running Services
All services are on `crewai-network` (172.19.0.x):

| Service | Container | IP | Ports | Status |
|---------|-----------|-------|-------|--------|
| Grafana | grafana | 172.19.0.5 | 3000 | ✓ Running |
| Consul (C2) | crewai-c2-dc1-prod-001-v1-0-0 | 172.19.0.6 | 8500, 9090 | ✓ Running |
| Prometheus | prometheus-working | 172.19.0.7 | 9095→9090 | ✓ Running |
| Fraud Sim API | host process | 172.17.0.1 | 8082 | ✓ Running |

### Network Configuration
- **Docker Network**: `crewai-network` (172.19.0.0/16)
- All containers connected to same network for service discovery
- Fraud Sim API runs on host, accessible via 172.17.0.1:8082

## Fraud Simulation Metrics

### Exposed Metrics (11 total)
Endpoint: http://localhost:8082/sim/metrics

```
fraud_sim_runs_total                      # Total runs created
fraud_sim_runs_in_progress                # Currently executing runs
fraud_sim_runs_completed                  # Successfully completed runs
fraud_sim_runs_failed                     # Failed runs
fraud_sim_last_run_accuracy              # Last run accuracy (0-1)
fraud_sim_last_run_precision             # Last run precision (0-1)
fraud_sim_last_run_recall                # Last run recall (0-1)
fraud_sim_last_run_f1_score              # Last run F1 score (0-1)
fraud_sim_total_transactions_analyzed    # Total transactions across all runs
fraud_sim_total_fraud_detected           # Total fraud detected across all runs
fraud_sim_pattern_flags{flag="..."}      # Pattern detection counts by type
```

### Pattern Flags
- `card_testing_small_amount` - Transactions < $5
- `card_testing_rapid_succession` - 5+ txns in <10 minutes
- `card_testing_mixed_decline_approve` - Mixed approval/decline patterns
- `card_testing_merchant_diversity` - 3+ merchants quickly

## Prometheus Configuration

### Scrape Configuration
File: `/tmp/prom-config-new.yml`

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'fraud-sim'
    static_configs:
      - targets: ['172.17.0.1:8082']
    metrics_path: '/sim/metrics'
```

### Verification Commands
```bash
# Check Prometheus targets
curl -s http://localhost:9095/api/v1/targets | python3 -m json.tool

# Query specific metric
curl -s 'http://localhost:9095/api/v1/query?query=fraud_sim_runs_total' | python3 -m json.tool

# Check all fraud sim metrics
curl -s 'http://localhost:9095/api/v1/label/__name__/values' | python3 -m json.tool | grep fraud_sim
```

## Grafana Dashboard

### Dashboard URL
**NEW WORKING DASHBOARD**: http://localhost:3000/d/d5c66783-3502-4e58-9377-1f2297a8e9ec/crewai-fraud-simulation-card-testing-detection

### Dashboard Files
- **Original** (no datasources): `metrics/fraud-sim-dashboard.json`
- **Fixed** (with datasources): `metrics/fraud-sim-dashboard-fixed.json`

### Datasource Configuration
- **Name**: Prometheus-Working
- **UID**: aeynydn98x7gge
- **Type**: prometheus
- **URL**: http://prometheus-working:9090
- **Access**: proxy

### Dashboard Panels (12 total)

| ID | Title | Type | Query |
|----|-------|------|-------|
| 1 | Total Runs | stat | fraud_sim_runs_total |
| 2 | Runs In Progress | stat | fraud_sim_runs_in_progress |
| 3 | Completed Runs | stat | fraud_sim_runs_completed |
| 4 | Failed Runs | stat | fraud_sim_runs_failed |
| 5 | Detection Performance Metrics | timeseries | accuracy, precision, recall, f1 |
| 6 | Pattern Flags Detected | bargauge | fraud_sim_pattern_flags |
| 7 | Last Run Accuracy | gauge | fraud_sim_last_run_accuracy |
| 8 | Last Run Precision | gauge | fraud_sim_last_run_precision |
| 9 | Last Run Recall | gauge | fraud_sim_last_run_recall |
| 10 | Total Transactions Analyzed | stat | fraud_sim_total_transactions_analyzed |
| 11 | Total Fraud Detected | stat | fraud_sim_total_fraud_detected |
| 12 | Run Completion Rate | timeseries | rate(fraud_sim_runs_completed[5m]) |

## Fraud Simulation API

### Server Process
**Command**: `python3 run_fraud_sim_server.py`
**PID**: Check with `ps aux | grep run_fraud_sim_server`
**Port**: 8082
**Log**: `/tmp/fraud_sim_server.log`

### API Endpoints

#### Create Run
```bash
curl -X POST http://localhost:8082/sim/run \
  -H "Content-Type: application/json" \
  -d '{
    "fraud_type": "card_testing",
    "transaction_count": 1000,
    "fraud_intensity": 0.10,
    "detection_threshold": 75
  }'
```

#### Get Status
```bash
curl http://localhost:8082/sim/status
```

#### List Runs
```bash
curl http://localhost:8082/sim/runs
```

#### Get Metrics
```bash
curl http://localhost:8082/sim/metrics
```

## Current Data Status

### Latest Run Results
```
Run ID: run_card_testing_1760888555
Transactions: 1000
Fraud Injected: 100 (10%)
Fraud Detected: 41

Confusion Matrix:
- True Positives: 41
- False Positives: 0
- True Negatives: 900
- False Negatives: 59

Performance:
- Accuracy: 94.1%
- Precision: 100%
- Recall: 41%
- F1 Score: 58.16%

Pattern Flags:
- card_testing_small_amount: 100
- card_testing_merchant_diversity: 58
- card_testing_mixed_decline_approve: 42
- card_testing_rapid_succession: 20
```

## Troubleshooting

### Metrics Not Showing in Dashboard
1. **Check fraud sim server is running**:
   ```bash
   curl http://localhost:8082/sim/metrics
   ```

2. **Check Prometheus is scraping**:
   ```bash
   curl -s http://localhost:9095/api/v1/targets | grep fraud-sim
   ```

3. **Check Grafana datasource**:
   ```bash
   curl -s -u admin:admin http://localhost:3000/api/datasources/3
   ```

4. **Test query through Grafana**:
   ```bash
   curl -s -u admin:admin 'http://localhost:3000/api/datasources/proxy/3/api/v1/query?query=fraud_sim_runs_total'
   ```

### Restart Services

#### Fraud Sim Server
```bash
pkill -f run_fraud_sim_server
cd /home/rreck/Desktop/202051018b/crewai-fraud-ach
nohup python3 run_fraud_sim_server.py > /tmp/fraud_sim_server.log 2>&1 &
```

#### Prometheus
```bash
docker restart prometheus-working
```

#### Grafana
```bash
docker restart grafana
```

## File Locations

### Code
- **Fraud Sim API**: `app/fraud_sim_api.py`
- **Run Manager**: `app/run_manager.py`
- **Card Testing Detector**: `app/card_testing_detector.py`
- **Synthetic Data Generator**: `app/synthetic_payment_generator.py`

### Configuration
- **Dashboard (Original)**: `metrics/fraud-sim-dashboard.json`
- **Dashboard (Fixed)**: `metrics/fraud-sim-dashboard-fixed.json`
- **Prometheus Config**: `/tmp/prom-config-new.yml`

### Data
- **Run Outputs**: `output/runs/run_*/`
- **PMEM Artifacts**: `kb/short/agent.fraud-sim.RESULT.*.md`

### Logs
- **Fraud Sim Server**: `/tmp/fraud_sim_server.log`
- **crewai-c2**: `docker logs crewai-c2-dc1-prod-001-v1-0-0`
- **Prometheus**: `docker logs prometheus-working`

## Verification Checklist

- [x] Fraud sim server running on port 8082
- [x] Metrics exposed at /sim/metrics
- [x] Prometheus scraping fraud sim metrics
- [x] Grafana datasource configured
- [x] Dashboard imported with proper datasources
- [x] All 12 panels have data
- [x] All containers on same network (crewai-network)
- [x] At least one successful run completed

## Next Steps

1. **Generate more runs** for time-series data:
   ```bash
   for i in {1..5}; do
     curl -X POST http://localhost:8082/sim/run \
       -H "Content-Type: application/json" \
       -d '{"fraud_type": "card_testing", "transaction_count": 500, "fraud_intensity": 0.15, "detection_threshold": 75}'
     sleep 2
   done
   ```

2. **Experiment with detection thresholds**:
   - Try threshold=50 for higher recall
   - Try threshold=85 for higher precision

3. **Adjust fraud intensity**:
   - 0.05 = 5% fraud (realistic)
   - 0.20 = 20% fraud (stress test)

4. **Monitor pattern flags** to tune detection rules
