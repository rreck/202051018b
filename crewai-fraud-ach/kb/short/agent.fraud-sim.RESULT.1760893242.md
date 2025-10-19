```json
{
  "id": "agent.fraud-sim.RESULT.1760893242",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760893242,
  "host_pid": "rreck-MS-7D25_260899",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T13:00:42",
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
    "accuracy": 0.9383,
    "precision": 1.0,
    "recall": 0.3833,
    "f1_score": 0.5542
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760893242"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760893242

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 600
- **Fraud Intensity**: 10.0%
- **Processing Time**: 0.09s

## Detection Results
- **True Positives**: 23
- **False Positives**: 0
- **True Negatives**: 540
- **False Negatives**: 37

## Performance Metrics
- **Accuracy**: 93.83%
- **Precision**: 100.00%
- **Recall**: 38.33%
- **F1 Score**: 55.42%

## Score Distribution
{
  "0-25": 569,
  "26-50": 7,
  "51-75": 12,
  "76-100": 12
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 60,
  "card_testing_merchant_diversity": 29,
  "card_testing_mixed_decline_approve": 24,
  "card_testing_rapid_succession": 12
}

## Analysis
This run successfully demonstrated card_testing detection capability with 93.8% accuracy.
The system correctly identified 23 of 60 fraudulent transactions.
