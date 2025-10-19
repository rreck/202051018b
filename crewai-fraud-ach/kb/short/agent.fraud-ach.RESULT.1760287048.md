```json
{
  "id": "ebf3f9245edcee4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287048,
  "host_pid": "9e6742732c60:1",
  "hash": "197943954f876b9a8ab14ad6a0001eba06b4b18e09858426b476ff022681236e",
  "cid": "QmV1197943954f876b9a8ab14ad6a0001eba06b4b18e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287048,
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
      "evaluated_at": 1760287048
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
  "sig": "2948d2785634eec3f51bb2ef8b0550cfcc0575381a33cbd03c7cfec3c5ba6536"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 111000028335360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 342102552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285764, 'matching_hash': '8e80efed4b38ef8e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7437012}}}