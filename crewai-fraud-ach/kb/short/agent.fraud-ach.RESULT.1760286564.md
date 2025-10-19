```json
{
  "id": "b70531b8f3ff7a3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286564,
  "host_pid": "9e6742732c60:1",
  "hash": "4a83970001847756fcdbe65d73a60f68fcad8e3ff05d2685f307d02d4887d79b",
  "cid": "QmV14a83970001847756fcdbe65d73a60f68fcad8e3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286564,
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
      "evaluated_at": 1760286564
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
  "sig": "a9897c25a33d60a888660e57fd52ebe29e3be11d0f0accc7dbbd64c947166566"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 111000025312922
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 166743504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285765, 'matching_hash': 'ec5c02804d9cd63b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5749776}}}