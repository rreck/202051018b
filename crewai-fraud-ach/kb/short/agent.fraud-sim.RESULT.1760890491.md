```json
{
  "id": "agent.fraud-sim.RESULT.1760890491",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760890491,
  "host_pid": "rreck-MS-7D25_230243",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T12:14:51",
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
    "accuracy": 0.94,
    "precision": 1.0,
    "recall": 0.4,
    "f1_score": 0.5714
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760890491"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760890491

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 800
- **Fraud Intensity**: 10.0%
- **Processing Time**: 0.03s

## Detection Results
- **True Positives**: 32
- **False Positives**: 0
- **True Negatives**: 720
- **False Negatives**: 48

## Performance Metrics
- **Accuracy**: 94.00%
- **Precision**: 100.00%
- **Recall**: 40.00%
- **F1 Score**: 57.14%

## Score Distribution
{
  "0-25": 753,
  "26-50": 15,
  "51-75": 16,
  "76-100": 16
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 80,
  "card_testing_merchant_diversity": 47,
  "card_testing_mixed_decline_approve": 32,
  "card_testing_rapid_succession": 16
}

## Analysis
This run successfully demonstrated card_testing detection capability with 94.0% accuracy.
The system correctly identified 32 of 80 fraudulent transactions.
