```json
{
  "id": "a8f72e0b68c17a4d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286270,
  "host_pid": "9e6742732c60:1",
  "hash": "51125e8b0016e5d63172a5489f948f9e541829a9f47d8c0f5b0fa0720f752da4",
  "cid": "QmV151125e8b0016e5d63172a5489f948f9e541829a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286270,
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
      "evaluated_at": 1760286270
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
  "sig": "f8d151e19c950e25150245ac4dd73ebb792fd1a6d11b8410a7edbb266389a618"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201465065641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 123229580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285763, 'matching_hash': 'c71bd5f7fa32abe1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6161479}}}