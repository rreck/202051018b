```json
{
  "id": "28a2313d6c91e058",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286360,
  "host_pid": "9e6742732c60:1",
  "hash": "b18933fc5ff86045de8e1b5a81d6596b3ddf2317c03c67d0950d053e0b61e98b",
  "cid": "QmV1b18933fc5ff86045de8e1b5a81d6596b3ddf2317",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286360,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286360
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "cf8d7c25b067b0c834c4ef51534d35a1a80b86f7d1e4ca7bcac44892b64955ac"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000026803563
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': 'cf30c88fa01e3081'}}}re': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '5b23ebe5172c1d5f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.53, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9306664}}}