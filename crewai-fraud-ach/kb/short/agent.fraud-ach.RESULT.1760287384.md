```json
{
  "id": "c42cc7eab3b552c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287384,
  "host_pid": "9e6742732c60:1",
  "hash": "252898e96f84334a8d5d8f2bc241e2148c0875632e4c714d8c11b945f7c54d1c",
  "cid": "QmV1252898e96f84334a8d5d8f2bc241e2148c087563",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287384,
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
      "evaluated_at": 1760287384
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
  "sig": "79a867338ccbfdd18acfb538549e31731937990e901fc5ce300802d289b4f541"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 121000242202372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 540750646, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285763, 'matching_hash': '7eed822364ae6d91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.54, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9323287}}}