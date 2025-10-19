```json
{
  "id": "d4e336332e22cb0a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286589,
  "host_pid": "9e6742732c60:1",
  "hash": "1d6c15028182d098735ce50696744551e5e5a1704ebfd04f3b8a958b099b4141",
  "cid": "QmV11d6c15028182d098735ce50696744551e5e5a170",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286589,
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
      "evaluated_at": 1760286589
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
  "sig": "729063993be35483baece3d68d1274dd8929f1cecccf3eadbf5a9343db91d158"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201467532863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 165430170, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285764, 'matching_hash': 'b320222423bba5e6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5514339}}}