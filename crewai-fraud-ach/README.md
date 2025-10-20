# CrewAI Fraud Detection & Simulation Agent — v1760962029

**Architecture:** Ronald P. Reck
**Copyright (c) RRECKTEK LLC**

An intelligent dual-mode fraud detection system that (1) analyzes ACH/NACHA transactions for fraud patterns, and (2) generates synthetic payment data with embedded fraud scenarios for model validation and confidence building. Features run-based simulations, multiple fraud types, pattern detection with scoring, confusion matrix analytics, and comprehensive Prometheus/Grafana integration with pmem 1.0 persistent memory architecture.

## 🚀 Features

### ACH Fraud Detection
- **🔍 Multi-Strategy Detection**: Velocity attacks, duplicates, anomalies, invalid routing numbers
- **📄 NACHA File Parsing**: Full ACH/NACHA format support with validation
- **🎯 Pattern Recognition**: Detects suspicious transaction patterns and anomalies
- **🧠 Biomimicry Memory (pmem 1.0)**: Persistent memory with cryptographic provenance tracking
- **📊 Real-time Analysis**: Processes ACH batches with concurrent transaction analysis

### Card Testing Fraud Simulation
- **🎲 Synthetic Data Generation**: Realistic 151-column payment transaction schema based on real-world data
- **💳 Multiple Fraud Types**: Card testing, velocity attacks, account takeover, synthetic identity
- **📈 Run-Based Simulations**: User-initiated fraud scenarios with configurable parameters
- **🎯 Detection Scoring**: 0-100 fraud scores with pattern flag explanations
- **📊 Confusion Matrix**: Ground truth comparison with TP/FP/TN/FN metrics
- **🔬 Model Validation**: Demonstrates detection capabilities without requiring real fraud data

### Infrastructure
- **🤖 A2A API Integration**: Standard CrewAI agent endpoints + fraud simulation endpoints
- **📈 Prometheus Metrics**: Comprehensive monitoring for both ACH analysis and fraud simulation
- **🎨 Grafana Dashboards**: Dual dashboards for ACH fraud detection and simulation performance
- **🔄 Deduplication**: SHA256-based caching prevents redundant processing
- **📁 Daemon & Watch Modes**: Background service or continuous monitoring capabilities
- **🔐 AICP Provenance**: Every artifact includes cryptographic proof of origin

## 📋 Quick Start

### ACH Fraud Detection
```bash
# Build and start daemon mode
cd crewai-fraud-ach
./run-fraud-ach-watch.sh build
./run-fraud-ach-watch.sh daemon

# Check status
./run-fraud-ach-watch.sh status
./run-fraud-ach-watch.sh health

# Process ACH files
cp your_file.ach input/
./run-fraud-ach-watch.sh trigger-batch

# Generate synthetic ACH data with embedded fraud
./run-fraud-ach-watch.sh generate-synthetic
```

### Card Testing Fraud Simulation
```bash
# Start fraud simulation server (runs on port 8082)
cd crewai-fraud-ach
python3 run_fraud_sim_server.py &

# Create a fraud simulation run
curl -X POST http://localhost:8082/sim/run \
  -H "Content-Type: application/json" \
  -d '{
    "fraud_type": "card_testing",
    "transaction_count": 1000,
    "fraud_intensity": 0.10,
    "detection_threshold": 75
  }'

# Check simulation status
curl http://localhost:8082/sim/status | jq

# View all completed runs
curl http://localhost:8082/sim/runs | jq

# View Grafana dashboard
# http://localhost:3000/d/d5c66783-3502-4e58-9377-1f2297a8e9ec
```

## 📁 Directory Structure

```
crewai-fraud-ach/
├── input/                          # ACH files for fraud analysis
│   └── *.ach, *.txt               # NACHA format files
├── output/                        # Analysis results and synthetic data
│   ├── *.fraud-analysis.json      # ACH fraud detection results
│   ├── *.synthetic.ach            # Generated synthetic ACH files
│   ├── *.synthetic.labels.json    # Fraud labels for synthetic data
│   ├── runs/                      # Fraud simulation run outputs
│   │   └── run_*/                 # Individual run directories
│   │       ├── config.json        # Run configuration
│   │       ├── transactions.csv   # Synthetic transaction data (151 columns)
│   │       ├── ground_truth.json  # Fraud labels for evaluation
│   │       ├── detection_results.json # Detection outputs with scores
│   │       └── metrics.json       # Performance metrics (TP/FP/TN/FN)
│   └── logs/                      # Processing logs and job cache
├── kb/                            # Biomimicry persistent memory (pmem 1.0)
│   ├── short/                     # Atomic notes and results (≤64KB)
│   │   ├── agent.fraud-ach.RESULT.*.md      # ACH detection results
│   │   ├── agent.fraud-sim.RESULT.*.md      # Simulation run results
│   │   ├── claude.TASK.*.md                 # Task definitions
│   │   └── claude.RESULT.*.md               # Implementation outcomes
│   └── long/                      # Rollups and emergent artifacts (≤512KB)
│       ├── CLUSTER.*.md           # Grouped patterns (≥5 sources)
│       ├── SYNTHESIS.*.md         # Cross-cluster insights
│       ├── META.*.md              # Meta-rules and standards
│       └── CONSENSUS.*.md         # Agreed-upon positions
├── app/
│   ├── main.py                    # Main ACH fraud detection agent
│   ├── ach_schema.py              # ACH/NACHA file parsing
│   ├── fraud_engine.py            # ACH fraud detection engine
│   ├── memory_system.py           # pmem 1.0 implementation
│   ├── synthetic_payment_generator.py # 151-column payment data generator
│   ├── card_testing_detector.py   # Card testing fraud detector
│   ├── run_manager.py             # Simulation run management
│   └── fraud_sim_api.py           # Fraud simulation API server
├── metrics/
│   ├── fraud-ach-dashboard.json   # ACH fraud detection dashboard
│   ├── fraud-sim-dashboard-fixed.json # Fraud simulation dashboard (12 panels)
│   └── prometheus.yml             # Prometheus scrape configuration
├── test_fraud_sim.py              # Standalone fraud simulation test
├── run_fraud_sim_server.py        # Fraud simulation API server launcher
├── Dockerfile                     # Container build definition
├── run-fraud-ach-watch.sh         # Container management script
├── requirements.txt               # Python dependencies
├── SETUP_DOCUMENTATION.md         # Complete infrastructure setup guide
├── CRITICAL_ISSUE_METRICS_PERSISTENCE.md # Known issue documentation
└── README.md                      # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `INPUT_DIR` | `./input` | Directory for ACH files |
| `OUTPUT_DIR` | `./output` | Directory for analysis results and synthetic data |
| `KB_DIR` | `./kb` | Knowledge base directory (pmem 1.0) |
| `API_PORT` | `8080` | A2A API server port (ACH agent) |
| `SIM_API_PORT` | `8082` | Fraud simulation API port |
| `METRICS_PORT` | `9090` | Prometheus metrics server port |
| `PIDFILE` | `/var/run/fraud-ach-agent.pid` | PID file for daemon mode |

### Container Ports

- **8080**: A2A API endpoints (health, job submission, batch processing)
- **8082**: Fraud simulation API (runs, status, metrics)
- **9090**: Prometheus metrics (`/metrics` endpoint)

## 🖥️ Usage

### ACH Fraud Detection

#### Container Management
```bash
# Start daemon mode (background service)
./run-fraud-ach-watch.sh daemon

# Start watch mode (foreground, Ctrl-C to stop)
./run-fraud-ach-watch.sh watch

# One-shot batch processing
./run-fraud-ach-watch.sh batch

# Check status and health
./run-fraud-ach-watch.sh status
./run-fraud-ach-watch.sh health

# View logs
./run-fraud-ach-watch.sh logs
./run-fraud-ach-watch.sh logs -f  # Follow logs

# Stop/restart container
./run-fraud-ach-watch.sh stop
./run-fraud-ach-watch.sh restart
```

#### Generate Synthetic ACH Data
```bash
# Generate ACH file with embedded fraud patterns
python3 app/main.py --generate --transactions 100 --fraud-ratio 0.05

# Output:
#   output/<timestamp>.synthetic.ach         # NACHA format file
#   output/<timestamp>.synthetic.labels.json # Fraud labels for testing
```

### Card Testing Fraud Simulation

#### Run Simulation via API
```bash
# Create simulation run (card testing)
curl -X POST http://localhost:8082/sim/run \
  -H "Content-Type: application/json" \
  -d '{
    "fraud_type": "card_testing",
    "transaction_count": 500,
    "fraud_intensity": 0.15,
    "detection_threshold": 75
  }'

# Create simulation run (velocity attack)
curl -X POST http://localhost:8082/sim/run \
  -H "Content-Type: application/json" \
  -d '{
    "fraud_type": "velocity_attack",
    "transaction_count": 500,
    "fraud_intensity": 0.10,
    "detection_threshold": 75
  }'

# Response includes:
# - run_id: Unique identifier
# - confusion_matrix: TP, FP, TN, FN
# - accuracy, precision, recall, f1_score
# - score_distribution: Histogram of fraud scores
# - pattern_flag_counts: Detection pattern breakdown
```

#### Run Simulation via Test Script
```bash
python3 test_fraud_sim.py
```

## 🔌 Agent-to-Agent (A2A) API

The agent provides HTTP endpoints for integration with other agents and automation workflows.

### ACH Fraud Detection Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/status` | Agent status and metrics |
| `GET` | `/config` | Current configuration |
| `POST` | `/job` | Process specific ACH file |
| `POST` | `/batch` | Trigger batch processing |
| `POST` | `/config` | Update configuration |

### Fraud Simulation Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/sim/status` | Simulation system status |
| `GET` | `/sim/runs` | List all simulation runs |
| `GET` | `/sim/run/{id}` | Get specific run details |
| `GET` | `/sim/metrics` | Prometheus-format metrics |
| `POST` | `/sim/run` | Create and execute new simulation run |

### Examples

#### ACH Processing
```bash
# Health check
curl http://localhost:8080/health

# Get status and metrics
curl http://localhost:8080/status | jq

# Process specific ACH file
curl -X POST http://localhost:8080/job \
  -H "Content-Type: application/json" \
  -d '{
    "file": "input/transactions.ach",
    "force": false
  }'

# Trigger batch processing
curl -X POST http://localhost:8080/batch
```

#### Fraud Simulation
```bash
# Create card testing simulation
curl -X POST http://localhost:8082/sim/run \
  -H "Content-Type: application/json" \
  -d '{
    "fraud_type": "card_testing",
    "transaction_count": 1000,
    "fraud_intensity": 0.10,
    "detection_threshold": 75
  }' | jq

# Get all runs
curl http://localhost:8082/sim/runs | jq

# Get specific run details
curl http://localhost:8082/sim/run/run_card_testing_1760888555 | jq

# Check system status
curl http://localhost:8082/sim/status | jq
```

## 📊 Data Schemas

### ACH Transaction Data

Standard NACHA file format with fields:
- **Transaction Code**: Debit/Credit indicator
- **Receiving DFI Routing Number**: 9-digit bank routing
- **Receiving DFI Account Number**: Account identifier
- **Amount**: Transaction amount in cents
- **Individual ID**: Customer identifier
- **Individual Name**: Account holder name
- **Trace Number**: Unique transaction trace
- **Addenda Records**: Additional transaction data

### Synthetic Payment Transaction Data (151 columns)

Based on `AISampleData.xlsx` schema from real payment systems:

#### Transaction Fields (Core)
- **TransactionID**: Unique transaction identifier
- **TransactionTypeID**: Transaction type code
- **CapturedDate**: Transaction capture timestamp
- **SettlementDate**: Settlement timestamp (1-3 days after capture)
- **Amount**: Transaction amount ($0.50 - $2000)
- **ConvenienceFee**: Additional fees
- **TransactionReferenceCode**: External reference
- **TransactionStatusTypeID**: Status (5=approved, 6=declined)

#### Card Fields
- **CreditCardAccountID**: Card account identifier
- **CardNumberMasked**: Masked PAN (XXXXXXXXXXXX7256 format)
- **CardNumberHashed**: SHA256 hash of card number
- **NameOnCard**: Cardholder name
- **ExpirationDate**: Card expiration (YYYYMMDD)
- **CreditCardTypeID**: Card brand (1=Visa, 2=MasterCard)
- **IssuingBankName**: Issuing financial institution

#### Customer Fields
- **CustomerID**: Unique customer identifier
- **FirstName, LastName**: Customer name
- **Email**: Customer email address
- **AddressLineOne, City, State, ZipCode**: Billing address
- **HomePhoneNumber**: Contact phone

#### Merchant Fields
- **MerchantID**: Merchant identifier
- **MerchantName**: Merchant business name
- **PayeeCode**: Merchant code
- **PayeeName**: Payee name

#### Organization Fields
- **OrganizationID**: Payment processor ID
- **OrganizationName**: Processor name

### Fraud Types & Patterns

#### 1. Card Testing
**Description**: Criminals test stolen card numbers with small transactions before making larger purchases.

**Characteristics**:
- Very small amounts ($0.50 - $5.00)
- Rapid succession (5+ transactions in <10 minutes)
- Same card used repeatedly
- Mixed approval/decline patterns
- Multiple different merchants

**Pattern Flags**:
- `card_testing_small_amount`: Transaction < $5.00
- `card_testing_rapid_succession`: 5+ txns in <10 minutes
- `card_testing_mixed_decline_approve`: Mix of status codes
- `card_testing_merchant_diversity`: 3+ different merchants quickly
- `card_testing_velocity`: >10 transactions/hour on same card

**Detection Score Range**: 76-100 (high confidence)

#### 2. Velocity Attack
**Description**: High-frequency transactions on same card to maximize theft before detection.

**Characteristics**:
- Many transactions in short timeframe (10+ per attack)
- Normal transaction amounts ($50-$300)
- Same card repeatedly
- All or most approved
- Compressed time window (5-15 minutes between transactions)

**Pattern Flags**:
- `velocity_attack_high_frequency`: >10 txns/hour
- `velocity_attack_sustained`: Attack continues over multiple periods

**Detection Score Range**: 70-90

#### 3. Account Takeover
**Description**: Attacker gains control of legitimate account and makes fraudulent purchases.

**Characteristics**:
- Unusual geographic location (different from account history)
- Large transaction amounts ($500-$2000)
- Different merchant patterns than typical
- Sudden change in spending behavior

**Pattern Flags**:
- `account_takeover_unusual_location`: Geographic anomaly
- `account_takeover_large_amount`: Amount significantly above normal

**Detection Score Range**: 80-100

#### 4. Synthetic Identity
**Description**: Fake identity created using mix of real and fabricated information.

**Characteristics**:
- Mismatched customer data (name doesn't match card name)
- Unusual name patterns (compound surnames)
- Generic/temporary email addresses
- High spend for "new" account
- No established transaction history

**Pattern Flags**:
- `synthetic_identity_mismatched_data`: Name/card mismatch
- `synthetic_identity_high_spend`: Unusual amount for new account

**Detection Score Range**: 75-95

### Fraud Simulation Distribution

#### Transaction Amounts
- **Legitimate Transactions**: $5 - $500 (normal distribution)
- **Large Legitimate**: $500 - $2000 (5% of legitimate transactions)
- **Card Testing Fraud**: $0.50 - $5.00
- **Velocity Attack Fraud**: $50 - $300
- **Account Takeover Fraud**: $500 - $2000
- **Synthetic Identity Fraud**: $300 - $1000

#### Geographic Distribution
36 US cities across all regions:
- **Major Metro**: New York, Los Angeles, Chicago, Houston, Phoenix
- **Tech Hubs**: San Francisco, Seattle, Austin, San Jose
- **Regional**: Nashville, Denver, Portland, Miami, Atlanta
- **Others**: Philadelphia, San Antonio, Dallas, Boston, Detroit, etc.

#### Card Issuers (14 major banks)
- Chase Bank, Bank of America, Wells Fargo, Citibank
- Capital One, US Bank, PNC Bank, TD Bank
- Truist Bank, Fifth Third Bank, Regions Bank
- Discover Bank, American Express, Synchrony Bank

#### Merchant Types (17 categories)
- **Retail**: Amazon, Walmart, Target, Costco, Best Buy
- **Pharmacy**: CVS, Walgreens
- **Grocery**: Kroger, Whole Foods
- **Food**: Starbucks, McDonald's
- **Fuel**: Shell Gas, Exxon
- **Streaming**: Netflix
- **Technology**: Apple, Microsoft

## 🎯 Detection Scoring System

### Fraud Score Calculation

Each transaction receives a fraud score from 0-100 based on pattern detection:

**Scoring Weights** (Card Testing Example):
- Small amount (<$5): +25 points
- Rapid succession (5+ in 10 min): +35 points
- Mixed decline/approve: +30 points
- Multiple merchants quickly: +20 points
- High transaction velocity: +25 points

**Score capped at 100**

### Risk Levels

| Score Range | Risk Level | Action |
|-------------|-----------|---------|
| 0-25 | **LOW** | Normal transaction, no flags |
| 26-50 | **MEDIUM-LOW** | Some suspicious patterns, monitor |
| 51-75 | **MEDIUM-HIGH** | Multiple suspicious patterns, review |
| 76-100 | **HIGH/CRITICAL** | Fraud detected, block/alert |

### Detection Threshold

Default: **75** (configurable per run)

- Scores ≥75: Flagged as fraud
- Scores <75: Passed as legitimate

### Confusion Matrix Metrics

**True Positive (TP)**: Correctly detected fraud
**False Positive (FP)**: Legitimate flagged as fraud
**True Negative (TN)**: Correctly passed legitimate
**False Negative (FN)**: Missed fraud

**Calculated Metrics**:
- **Accuracy** = (TP + TN) / Total
- **Precision** = TP / (TP + FP)
- **Recall** = TP / (TP + FN)
- **F1 Score** = 2 × (Precision × Recall) / (Precision + Recall)

### Typical Performance

**Card Testing Detection**:
- Accuracy: 90-95%
- Precision: 95-100%
- Recall: 35-45%
- F1 Score: 50-60%

**Note**: High precision (few false positives) prioritized over recall to minimize customer friction.

## 📈 Prometheus Metrics

### ACH Fraud Detection Metrics

Access at `http://localhost:9090/metrics`

| Metric | Type | Description |
|--------|------|-------------|
| `fraud_ach_files_processed_total` | Counter | ACH files successfully processed |
| `fraud_ach_files_failed_total` | Counter | ACH files that failed processing |
| `fraud_ach_transactions_analyzed_total` | Counter | Total ACH transactions analyzed |
| `fraud_ach_fraud_detected_total` | Counter | Total fraud cases detected |
| `fraud_ach_fraud_by_type` | Counter | Fraud detections by type (velocity_attack, duplicate, anomaly, invalid_routing) |
| `fraud_ach_memory_artifacts_total` | Counter | pmem 1.0 artifacts created |
| `fraud_ach_daemon_uptime_seconds` | Gauge | Agent uptime |

### Fraud Simulation Metrics

Access at `http://localhost:8082/sim/metrics`

| Metric | Type | Description |
|--------|------|-------------|
| `fraud_sim_runs_total` | Counter | Total simulation runs created |
| `fraud_sim_runs_in_progress` | Gauge | Runs currently executing |
| `fraud_sim_runs_completed` | Counter | Successfully completed runs |
| `fraud_sim_runs_failed` | Counter | Failed runs |
| `fraud_sim_last_run_accuracy` | Gauge | Most recent run accuracy (0-1) |
| `fraud_sim_last_run_precision` | Gauge | Most recent run precision (0-1) |
| `fraud_sim_last_run_recall` | Gauge | Most recent run recall (0-1) |
| `fraud_sim_last_run_f1_score` | Gauge | Most recent run F1 score (0-1) |
| `fraud_sim_total_transactions_analyzed` | Counter | Cumulative transactions across all runs |
| `fraud_sim_total_fraud_detected` | Counter | Cumulative fraud detected across all runs |
| `fraud_sim_pattern_flags` | Gauge | Pattern flag counts by type |
| `fraud_sim_run_accuracy` | Gauge | Per-run accuracy with run_id and fraud_type labels |
| `fraud_sim_run_precision` | Gauge | Per-run precision with run_id and fraud_type labels |
| `fraud_sim_run_recall` | Gauge | Per-run recall with run_id and fraud_type labels |
| `fraud_sim_run_f1_score` | Gauge | Per-run F1 score with run_id and fraud_type labels |

### Grafana Dashboards

#### ACH Fraud Detection Dashboard
Located at: `metrics/fraud-ach-dashboard.json`

**6 Panels**:
1. Files Processed (stat)
2. Fraud Detection Rate (gauge)
3. Transactions Analyzed (time-series)
4. Fraud by Type (pie chart)
5. Memory Artifacts (stat)
6. Agent Uptime (stat)

#### Fraud Simulation Dashboard
**URL**: http://localhost:3000/d/d5c66783-3502-4e58-9377-1f2297a8e9ec
Located at: `metrics/fraud-sim-dashboard-fixed.json`

**12 Panels**:
1. **Total Runs** (stat) - fraud_sim_runs_total
2. **Runs In Progress** (stat) - fraud_sim_runs_in_progress
3. **Completed Runs** (stat) - fraud_sim_runs_completed
4. **Failed Runs** (stat) - fraud_sim_runs_failed
5. **Detection Performance Metrics** (time-series) - accuracy, precision, recall, F1
6. **Pattern Flags Detected** (bar gauge) - fraud_sim_pattern_flags
7. **Last Run Accuracy** (gauge 0-100%) - fraud_sim_last_run_accuracy
8. **Last Run Precision** (gauge 0-100%) - fraud_sim_last_run_precision
9. **Last Run Recall** (gauge 0-100%) - fraud_sim_last_run_recall
10. **Total Transactions Analyzed** (stat) - fraud_sim_total_transactions_analyzed
11. **Total Fraud Detected** (stat) - fraud_sim_total_fraud_detected
12. **Run Completion Rate** (time-series) - rate(fraud_sim_runs_completed[5m])

### Example PromQL Queries

```promql
# Average fraud detection accuracy across last 10 runs
avg_over_time(fraud_sim_last_run_accuracy[1h])

# Total fraud detected per hour
rate(fraud_sim_total_fraud_detected[1h]) * 3600

# Pattern flag distribution
topk(5, fraud_sim_pattern_flags)

# Fraud detection success rate (precision)
fraud_sim_last_run_precision

# Run completion rate (runs per minute)
rate(fraud_sim_runs_completed[5m]) * 60

# Compare accuracy across fraud types
fraud_sim_run_accuracy{fraud_type="card_testing"}
fraud_sim_run_accuracy{fraud_type="velocity_attack"}
fraud_sim_run_accuracy{fraud_type="account_takeover"}
fraud_sim_run_accuracy{fraud_type="synthetic_identity"}
```

## 🧠 Persistent Memory (pmem 1.0)

### Architecture

Biomimicry-driven persistent memory system with:

- **Cryptographic Provenance**: Every artifact includes AICP (prov, ucon, eval) headers
- **Structured Filenames**: `{scope}.{KEY}.{EPOCH}.md`
- **Bidirectional Links**: Sources and edges tracked with weights
- **Weight Decay**: Edge weights decay over time (λ=0.01/day, clip w∈[0,1])
- **Emergent Learning**: Clusters, synthesis, meta-rules form from patterns

### Artifact Types

| Type | Description | Threshold |
|------|-------------|-----------|
| **RESULT** | Detection results, simulation outcomes | N/A |
| **TASK** | Task definitions and plans | N/A |
| **PROBLEM** | Issues and blockers | N/A |
| **LESSON** | Learnings from runs | N/A |
| **CLUSTER** | Grouped patterns | ≥5 sources, w≥0.6 |
| **SYNTHESIS** | Cross-cluster insights | ≥2 clusters, JS≤0.25 |
| **META** | Meta-rules and standards | N/A |
| **ECHO** | Replay and mutation detection | N/A |
| **CONSENSUS** | Agreed-upon positions | ≥67% quorum |

### File Naming Convention

```
{scope}.{KEY}.{EPOCH}.md

scope  ∈ {agent, crew, claude}
KEY    ∈ {RESULT, TASK, PROBLEM, LESSON, CLUSTER, SYNTHESIS, META, ECHO, CONSENSUS}
EPOCH  = Unix timestamp (seconds)
```

**Examples**:
- `agent.fraud-sim.RESULT.1760888555.md` - Simulation run result
- `claude.TASK.1760886964.md` - Implementation task
- `agent.fraud-ach.RESULT.1760284664.md` - ACH detection result

### AICP Header Format

Every artifact includes JSON header:

```json
{
  "id": "agent.fraud-sim.RESULT.1760888555",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760888555,
  "host_pid": "hostname_12345",
  "hash": "sha256_hash",
  "cid": "content_id",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T11:24:24Z",
      "proof": "ed25519:signature"
    },
    "ucon": {
      "constraints": ["synthetic-data-only", "test-environment"],
      "obligations": ["track-detection-accuracy"]
    },
    "eval": {
      "risk": "low",
      "classification": "simulation",
      "review_required": false
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {
    "accuracy": 0.941,
    "precision": 1.0,
    "recall": 0.41,
    "f1_score": 0.5816
  },
  "thresholds": {},
  "tags": ["card_testing", "simulation"],
  "sig": "signature"
}
```

### Consolidation Rules

**Co-occurrence Window**: τ=7 days
**Weight Decay**: λ=0.01/day
**Cluster Formation**: ≥5 sources, w≥0.6
**Synthesis Threshold**: ≥2 clusters, JS divergence ≤0.25
**Consensus Quorum**: ≥67% agreement

**File Size Limits**:
- Atomic notes (short/): ≤64 KB
- Rollups (long/): ≤512 KB

## 🔍 Debugging and Troubleshooting

### Quick Health Checks

```bash
# Check ACH agent
./run-fraud-ach-watch.sh status
./run-fraud-ach-watch.sh health

# Check fraud simulation server
curl http://localhost:8082/sim/status | jq

# Test API endpoints
curl -f http://localhost:8080/health
curl -f http://localhost:8082/sim/status
curl -f http://localhost:9090/metrics
```

### View Logs

```bash
# ACH agent container logs
./run-fraud-ach-watch.sh logs -f

# Fraud simulation server logs
tail -f /tmp/fraud_sim_server.log

# Processing logs
ls -la output/logs/
tail -f output/logs/*.log
```

### Common Issues

**Metrics Reset on Restart (CRITICAL)**:
- **Problem**: fraud_sim server stores metrics in memory only
- **Symptom**: `runs_total` shows fewer runs than exist in `output/runs/`
- **Root Cause**: No persistence between restarts
- **Workaround**: None - data lost on restart
- **Fix Required**: See `CRITICAL_ISSUE_METRICS_PERSISTENCE.md`

**Dashboard Shows No Data**:
1. Check fraud sim server is running: `curl http://localhost:8082/sim/status`
2. Check Prometheus is scraping: `curl http://localhost:9095/api/v1/targets | grep fraud-sim`
3. Verify Grafana datasource: Check http://localhost:3000/datasources
4. Wait 15 seconds for Prometheus scrape cycle
5. Create a test run to generate new metrics

**ACH File Processing Failures**:
- Verify file is valid NACHA format
- Check file permissions
- Review logs in `output/logs/`
- Ensure sufficient disk space

**API Connection Issues**:
- Check ports 8080/8082/9090 availability: `netstat -tulpn | grep -E '(8080|8082|9090)'`
- Verify containers are running: `docker ps`
- Check Docker network: All containers must be on `crewai-network`
- Test health endpoints directly

### Manual Testing

```bash
# Test fraud simulation
cd crewai-fraud-ach
python3 test_fraud_sim.py

# Test specific fraud type
curl -X POST http://localhost:8082/sim/run \
  -H "Content-Type: application/json" \
  -d '{"fraud_type":"velocity_attack","transaction_count":300,"fraud_intensity":0.15,"detection_threshold":75}' | jq

# Verify output files
ls -la output/runs/run_*/
cat output/runs/run_*/metrics.json | jq
```

## ⚠️ Known Issues

### CRITICAL: Metrics Persistence Failure

**Status**: UNRESOLVED
**Severity**: HIGH
**Impact**: Production deployment BLOCKED

See `CRITICAL_ISSUE_METRICS_PERSISTENCE.md` for full details.

**Summary**:
- Fraud simulation metrics stored in memory only
- Server restart loses all historical run data
- Dashboard shows incomplete information
- Prometheus counters violate monotonic increase rule

**Required Fix**: Implement `_load_existing_runs()` in `FraudSimMetrics.__init__()`

## 📝 Development

### Dependencies

Python 3.11+ required

**Core**:
- `requests` - HTTP API calls
- `python-daemon` - Daemon mode support

**Standard Library**:
- `json`, `csv`, `hashlib`, `datetime`
- `threading`, `http.server`, `concurrent.futures`
- `dataclasses`, `pathlib`

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Or in container
./run-fraud-ach-watch.sh build
```

## 📜 License

Copyright (c) RRECKTEK LLC. All rights reserved.

## 🆘 Support

**Before requesting support**:
1. Check logs: `./run-fraud-ach-watch.sh logs`
2. Validate configuration: `curl http://localhost:8082/sim/status`
3. Test health endpoints: All should return HTTP 200
4. Review `SETUP_DOCUMENTATION.md` for infrastructure details
5. Check `CRITICAL_ISSUE_METRICS_PERSISTENCE.md` for known issues

## 📚 Additional Documentation

- **SETUP_DOCUMENTATION.md**: Complete infrastructure setup and troubleshooting
- **CRITICAL_ISSUE_METRICS_PERSISTENCE.md**: Metrics persistence failure analysis and fix
- **CLAUDE.md**: Development guidelines and architecture patterns
- **PMEM.md**: Persistent memory (pmem 1.0) specification

---

**Quick Start Summary:**

**Fraud Simulation (Recommended for Testing)**:
1. `python3 run_fraud_sim_server.py &` - Start simulation server
2. Create run: `curl -X POST http://localhost:8082/sim/run -H "Content-Type: application/json" -d '{"fraud_type":"card_testing","transaction_count":500,"fraud_intensity":0.10,"detection_threshold":75}'`
3. View dashboard: http://localhost:3000/d/d5c66783-3502-4e58-9377-1f2297a8e9ec
4. Check metrics: `curl http://localhost:8082/sim/metrics`

**ACH Fraud Detection (Production)**:
1. `./run-fraud-ach-watch.sh build` - Build container
2. `./run-fraud-ach-watch.sh daemon` - Start agent
3. Place ACH files in `input/`
4. `./run-fraud-ach-watch.sh trigger-batch` - Process files
5. Check `output/` for fraud analysis results

**Monitoring**:
- Prometheus: http://localhost:9095
- Grafana: http://localhost:3000
- Fraud Sim Metrics: http://localhost:8082/sim/metrics
- ACH Agent Status: `curl http://localhost:8080/status`
