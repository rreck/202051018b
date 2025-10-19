```json
{
  "id": "agent.fraud-sim.RESULT.1760888555",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760888555,
  "host_pid": "rreck-MS-7D25_230243",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T11:42:35",
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
    "accuracy": 0.941,
    "precision": 1.0,
    "recall": 0.41,
    "f1_score": 0.5816
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760888555"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760888555

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 1000
- **Fraud Intensity**: 10.0%
- **Processing Time**: 0.04s

## Detection Results
- **True Positives**: 41
- **False Positives**: 0
- **True Negatives**: 900
- **False Negatives**: 59

## Performance Metrics
- **Accuracy**: 94.10%
- **Precision**: 100.00%
- **Recall**: 41.00%
- **F1 Score**: 58.16%

## Score Distribution
{
  "0-25": 941,
  "26-50": 17,
  "51-75": 22,
  "76-100": 20
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 100,
  "card_testing_merchant_diversity": 58,
  "card_testing_mixed_decline_approve": 42,
  "card_testing_rapid_succession": 20
}

## Analysis
This run successfully demonstrated card_testing detection capability with 94.1% accuracy.
The system correctly identified 41 of 100 fraudulent transactions.
