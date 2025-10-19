```json
{
  "id": "agent.fraud-sim.RESULT.1760894377",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760894377,
  "host_pid": "rreck-MS-7D25_267067",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T13:19:37",
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
    "run_run_synthetic_identity_1760894377"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_synthetic_identity_1760894377

## Configuration
- **Fraud Type**: synthetic_identity
- **Transaction Count**: 400
- **Fraud Intensity**: 10.0%
- **Processing Time**: 0.01s

## Detection Results
- **True Positives**: 0
- **False Positives**: 0
- **True Negatives**: 360
- **False Negatives**: 40

## Performance Metrics
- **Accuracy**: 90.00%
- **Precision**: 0.00%
- **Recall**: 0.00%
- **F1 Score**: 0.00%

## Score Distribution
{
  "0-25": 400,
  "26-50": 0,
  "51-75": 0,
  "76-100": 0
}

## Pattern Flags Detected
{}

## Analysis
This run successfully demonstrated synthetic_identity detection capability with 90.0% accuracy.
The system correctly identified 0 of 40 fraudulent transactions.
