```json
{
  "id": "agent.fraud-sim.RESULT.1760893232",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760893232,
  "host_pid": "rreck-MS-7D25_260899",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T13:00:32",
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
    "accuracy": 0.945,
    "precision": 1.0,
    "recall": 0.4,
    "f1_score": 0.5714
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760893232"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760893232

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 600
- **Fraud Intensity**: 9.2%
- **Processing Time**: 0.02s

## Detection Results
- **True Positives**: 22
- **False Positives**: 0
- **True Negatives**: 545
- **False Negatives**: 33

## Performance Metrics
- **Accuracy**: 94.50%
- **Precision**: 100.00%
- **Recall**: 40.00%
- **F1 Score**: 57.14%

## Score Distribution
{
  "0-25": 568,
  "26-50": 9,
  "51-75": 12,
  "76-100": 11
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 55,
  "card_testing_mixed_decline_approve": 23,
  "card_testing_merchant_diversity": 31,
  "card_testing_rapid_succession": 11
}

## Analysis
This run successfully demonstrated card_testing detection capability with 94.5% accuracy.
The system correctly identified 22 of 55 fraudulent transactions.
