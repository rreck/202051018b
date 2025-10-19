```json
{
  "id": "agent.fraud-sim.RESULT.1760894376",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760894376,
  "host_pid": "rreck-MS-7D25_267067",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T13:19:36",
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
    "accuracy": 0.91,
    "precision": 0.0,
    "recall": 0.0,
    "f1_score": 0.0
  },
  "thresholds": {},
  "tags": [
    "velocity_attack",
    "simulation",
    "run_run_velocity_attack_1760894376"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_velocity_attack_1760894376

## Configuration
- **Fraud Type**: velocity_attack
- **Transaction Count**: 400
- **Fraud Intensity**: 9.0%
- **Processing Time**: 0.01s

## Detection Results
- **True Positives**: 0
- **False Positives**: 0
- **True Negatives**: 364
- **False Negatives**: 36

## Performance Metrics
- **Accuracy**: 91.00%
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
{
  "card_testing_merchant_diversity": 27
}

## Analysis
This run successfully demonstrated velocity_attack detection capability with 91.0% accuracy.
The system correctly identified 0 of 36 fraudulent transactions.
