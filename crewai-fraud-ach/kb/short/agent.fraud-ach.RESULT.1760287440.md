```json
{
  "id": "aa43db10c86c37af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287440,
  "host_pid": "9e6742732c60:1",
  "hash": "78f21937795666ef71eda538cbd3109a33f9499db7c8952405dbce18c2a004fc",
  "cid": "QmV178f21937795666ef71eda538cbd3109a33f9499d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287440,
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
      "evaluated_at": 1760287440
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
  "sig": "01213941346d96586f99851522b768b26a4e817e6b778c78fca98048eeddf746"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 063100279293429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 314356080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285763, 'matching_hash': 'f44f07036b33cc03'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5239268}}}