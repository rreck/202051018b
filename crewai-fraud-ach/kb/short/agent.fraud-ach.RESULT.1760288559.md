```json
{
  "id": "2f72a2d093aed2a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288559,
  "host_pid": "9e6742732c60:1",
  "hash": "272efee98d4895e2f756d37a1e4b6c4a2f1997da482db981d1b44b6765d23d72",
  "cid": "QmV1272efee98d4895e2f756d37a1e4b6c4a2f1997da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288559,
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
      "evaluated_at": 1760288559
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "86a123575c59e6ad065dcfc401082edf708e47c5e92b6d3bbc7247577fd4e7c7"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 031201462613659
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 599307904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285764, 'matching_hash': '5c1e39699924121a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6178432}}}