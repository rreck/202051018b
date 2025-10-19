```json
{
  "id": "d0223e0ed352e3db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286845,
  "host_pid": "9e6742732c60:1",
  "hash": "7d2c546d65b6b191a23a07675904eb910661f3d7d4637e99b7c9abff57827ea7",
  "cid": "QmV17d2c546d65b6b191a23a07675904eb910661f3d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286845,
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
      "evaluated_at": 1760286845
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "f0fa10ab36aee7121335ea749e928a42dc3b9b5cd7855fbd012ff2f1f07dfd7a"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201462394531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 297845730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '046e1c7f2d74b138'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7637070}}}