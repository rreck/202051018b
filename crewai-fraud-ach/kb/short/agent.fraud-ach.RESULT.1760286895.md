```json
{
  "id": "0c0fd61887fa4710",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286895,
  "host_pid": "9e6742732c60:1",
  "hash": "9274b51b8237dd91f4a52c8e5ecbb820e5efd025a823e1d820c318bbd361fc52",
  "cid": "QmV19274b51b8237dd91f4a52c8e5ecbb820e5efd025",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286895,
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
      "evaluated_at": 1760286895
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
  "sig": "be8e8e8206143931e653744eb25f17ebb6e2ac8f35ba72edcbd7b793a716b79b"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 021000028707079
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 280844957, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285764, 'matching_hash': '67ae9df98d5fdee3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6849877}}}