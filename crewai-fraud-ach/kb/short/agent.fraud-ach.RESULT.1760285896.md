```json
{
  "id": "8525216a60e44e2d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285896,
  "host_pid": "9e6742732c60:1",
  "hash": "71885ef57fec47c15ac95ccc0d34bac98e380fb3352bb8ebfa2f688eac63988c",
  "cid": "QmV171885ef57fec47c15ac95ccc0d34bac98e380fb3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285896,
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
      "evaluated_at": 1760285896
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
  "sig": "b752485ed41a0c7c25eb8bbdd286253b7a99059bb142367f3bb5a08f5c7dc1de"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201467532863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 38600373, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285764, 'matching_hash': 'b320222423bba5e6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5514339}}}