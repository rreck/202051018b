```json
{
  "id": "f2546d8eb02a721e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286533,
  "host_pid": "9e6742732c60:1",
  "hash": "cc74584cc60f06078c2489e86ce5233275c89268fa10a4d1f7d89dbf4ebd1cd4",
  "cid": "QmV1cc74584cc60f06078c2489e86ce5233275c89268",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286533,
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
      "evaluated_at": 1760286533
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
  "sig": "3b938c80781d64c9046e7cdcdacea0ca26af8edb196315f22d1cfde2d1d9ad00"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 111000026237439
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 152939556, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285765, 'matching_hash': '88704d1e07f02084'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5462127}}}