```json
{
  "id": "agent.fraud-sim.RESULT.1760894200",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760894200,
  "host_pid": "rreck-MS-7D25_267067",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T13:16:40",
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
    "accuracy": 0.95,
    "precision": 1.0,
    "recall": 0.375,
    "f1_score": 0.5455
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760894200"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760894200

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 500
- **Fraud Intensity**: 8.0%
- **Processing Time**: 0.02s

## Detection Results
- **True Positives**: 15
- **False Positives**: 0
- **True Negatives**: 460
- **False Negatives**: 25

## Performance Metrics
- **Accuracy**: 95.00%
- **Precision**: 100.00%
- **Recall**: 37.50%
- **F1 Score**: 54.55%

## Score Distribution
{
  "0-25": 478,
  "26-50": 5,
  "51-75": 9,
  "76-100": 8
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 40,
  "card_testing_merchant_diversity": 19,
  "card_testing_mixed_decline_approve": 17,
  "card_testing_rapid_succession": 8
}

## Analysis
This run successfully demonstrated card_testing detection capability with 95.0% accuracy.
The system correctly identified 15 of 40 fraudulent transactions.
