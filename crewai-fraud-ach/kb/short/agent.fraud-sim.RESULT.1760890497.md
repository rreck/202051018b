```json
{
  "id": "agent.fraud-sim.RESULT.1760890497",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760890497,
  "host_pid": "rreck-MS-7D25_230243",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T12:14:57",
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
    "accuracy": 0.9363,
    "precision": 1.0,
    "recall": 0.4,
    "f1_score": 0.5714
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760890497"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760890497

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 800
- **Fraud Intensity**: 10.6%
- **Processing Time**: 0.03s

## Detection Results
- **True Positives**: 34
- **False Positives**: 0
- **True Negatives**: 715
- **False Negatives**: 51

## Performance Metrics
- **Accuracy**: 93.63%
- **Precision**: 100.00%
- **Recall**: 40.00%
- **F1 Score**: 57.14%

## Score Distribution
{
  "0-25": 749,
  "26-50": 15,
  "51-75": 19,
  "76-100": 17
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 85,
  "card_testing_merchant_diversity": 49,
  "card_testing_mixed_decline_approve": 36,
  "card_testing_rapid_succession": 17
}

## Analysis
This run successfully demonstrated card_testing detection capability with 93.6% accuracy.
The system correctly identified 34 of 85 fraudulent transactions.
