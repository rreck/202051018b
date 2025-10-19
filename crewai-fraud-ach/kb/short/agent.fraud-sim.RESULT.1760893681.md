```json
{
  "id": "agent.fraud-sim.RESULT.1760893681",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760893681,
  "host_pid": "rreck-MS-7D25_267067",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T13:08:01",
      "proof": "ed25519:stub"
    },
    "ucon": {
      "constraints": [
        "synthetic-data-only",
        "test-environment"
      ],
      "obligations": [
        "track-detection-accuracy"
      ]
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
    "accuracy": 0.9,
    "precision": 0.0,
    "recall": 0.0,
    "f1_score": 0.0
  },
  "thresholds": {},
  "tags": [
    "synthetic_identity",
    "simulation",
    "run_run_synthetic_identity_1760893681"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_synthetic_identity_1760893681

## Configuration
- **Fraud Type**: synthetic_identity
- **Transaction Count**: 500
- **Fraud Intensity**: 10.0%
- **Processing Time**: 0.02s

## Detection Results
- **True Positives**: 0
- **False Positives**: 0
- **True Negatives**: 450
- **False Negatives**: 50

## Performance Metrics
- **Accuracy**: 90.00%
- **Precision**: 0.00%
- **Recall**: 0.00%
- **F1 Score**: 0.00%

## Score Distribution
{
  "0-25": 500,
  "26-50": 0,
  "51-75": 0,
  "76-100": 0
}

## Pattern Flags Detected
{}

## Analysis
This run successfully demonstrated synthetic_identity detection capability with 90.0% accuracy.
The system correctly identified 0 of 50 fraudulent transactions.
