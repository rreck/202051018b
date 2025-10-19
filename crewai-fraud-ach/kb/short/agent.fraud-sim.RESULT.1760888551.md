```json
{
  "id": "agent.fraud-sim.RESULT.1760888551",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760888551,
  "host_pid": "rreck-MS-7D25_230243",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T11:42:31",
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
    "accuracy": 0.939,
    "precision": 1.0,
    "recall": 0.39,
    "f1_score": 0.5612
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760888551"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760888551

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 1000
- **Fraud Intensity**: 10.0%
- **Processing Time**: 0.04s

## Detection Results
- **True Positives**: 39
- **False Positives**: 0
- **True Negatives**: 900
- **False Negatives**: 61

## Performance Metrics
- **Accuracy**: 93.90%
- **Precision**: 100.00%
- **Recall**: 39.00%
- **F1 Score**: 56.12%

## Score Distribution
{
  "0-25": 942,
  "26-50": 17,
  "51-75": 21,
  "76-100": 20
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 100,
  "card_testing_merchant_diversity": 56,
  "card_testing_mixed_decline_approve": 41,
  "card_testing_rapid_succession": 20
}

## Analysis
This run successfully demonstrated card_testing detection capability with 93.9% accuracy.
The system correctly identified 39 of 100 fraudulent transactions.
