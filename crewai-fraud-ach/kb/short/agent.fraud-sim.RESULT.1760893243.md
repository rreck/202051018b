```json
{
  "id": "agent.fraud-sim.RESULT.1760893243",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760893243,
  "host_pid": "rreck-MS-7D25_260899",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T13:00:43",
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
    "accuracy": 0.9433,
    "precision": 1.0,
    "recall": 0.3818,
    "f1_score": 0.5526
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760893243"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760893243

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 600
- **Fraud Intensity**: 9.2%
- **Processing Time**: 0.02s

## Detection Results
- **True Positives**: 21
- **False Positives**: 0
- **True Negatives**: 545
- **False Negatives**: 34

## Performance Metrics
- **Accuracy**: 94.33%
- **Precision**: 100.00%
- **Recall**: 38.18%
- **F1 Score**: 55.26%

## Score Distribution
{
  "0-25": 571,
  "26-50": 7,
  "51-75": 11,
  "76-100": 11
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 55,
  "card_testing_mixed_decline_approve": 22,
  "card_testing_merchant_diversity": 27,
  "card_testing_rapid_succession": 11
}

## Analysis
This run successfully demonstrated card_testing detection capability with 94.3% accuracy.
The system correctly identified 21 of 55 fraudulent transactions.
