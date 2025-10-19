```json
{
  "id": "agent.fraud-sim.RESULT.1760890502",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760890502,
  "host_pid": "rreck-MS-7D25_230243",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T12:15:02",
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
    "accuracy": 0.9437,
    "precision": 1.0,
    "recall": 0.4,
    "f1_score": 0.5714
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760890502"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760890502

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 800
- **Fraud Intensity**: 9.4%
- **Processing Time**: 0.03s

## Detection Results
- **True Positives**: 30
- **False Positives**: 0
- **True Negatives**: 725
- **False Negatives**: 45

## Performance Metrics
- **Accuracy**: 94.37%
- **Precision**: 100.00%
- **Recall**: 40.00%
- **F1 Score**: 57.14%

## Score Distribution
{
  "0-25": 758,
  "26-50": 11,
  "51-75": 16,
  "76-100": 15
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 75,
  "card_testing_merchant_diversity": 41,
  "card_testing_mixed_decline_approve": 31,
  "card_testing_rapid_succession": 15
}

## Analysis
This run successfully demonstrated card_testing detection capability with 94.4% accuracy.
The system correctly identified 30 of 75 fraudulent transactions.
