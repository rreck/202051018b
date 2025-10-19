```json
{
  "id": "91a2b8ca4bbd3337",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292946,
  "host_pid": "9e6742732c60:1",
  "hash": "e8f44499c95d729984239afcbc142818ef51de975d1a6b6b19e8a1b2a03a0ccf",
  "cid": "QmV1e8f44499c95d729984239afcbc142818ef51de97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292946,
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
      "evaluated_at": 1760292946
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
  "sig": "2642664c7de874b7f6a8ff55dbda10068c435ef7bafb5b9ca8af66ce95de552d"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 031201462394531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 1588510560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': '046e1c7f2d74b138'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.94, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7637070}}}