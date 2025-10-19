```json
{
  "id": "agent.fraud-sim.RESULT.1760887464",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760887464,
  "host_pid": "rreck-MS-7D25_222760",
  "hash": "stub_hash",
  "cid": "stub_cid",
  "aicp": {
    "prov": {
      "issuer": "did:agent:fraud-sim",
      "issued": "2025-10-19T11:24:24",
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
    "accuracy": 0.916,
    "precision": 1.0,
    "recall": 0.4,
    "f1_score": 0.5714
  },
  "thresholds": {},
  "tags": [
    "card_testing",
    "simulation",
    "run_run_card_testing_1760887464"
  ],
  "sig": "stub_signature"
}
```

# Fraud Simulation Run: run_card_testing_1760887464

## Configuration
- **Fraud Type**: card_testing
- **Transaction Count**: 500
- **Fraud Intensity**: 14.0%
- **Processing Time**: 0.02s

## Detection Results
- **True Positives**: 28
- **False Positives**: 0
- **True Negatives**: 430
- **False Negatives**: 42

## Performance Metrics
- **Accuracy**: 91.60%
- **Precision**: 100.00%
- **Recall**: 40.00%
- **F1 Score**: 57.14%

## Score Distribution
{
  "0-25": 459,
  "26-50": 12,
  "51-75": 15,
  "76-100": 14
}

## Pattern Flags Detected
{
  "card_testing_small_amount": 70,
  "card_testing_merchant_diversity": 40,
  "card_testing_mixed_decline_approve": 29,
  "card_testing_rapid_succession": 14
}

## Analysis
This run successfully demonstrated card_testing detection capability with 91.6% accuracy.
The system correctly identified 28 of 70 fraudulent transactions.
