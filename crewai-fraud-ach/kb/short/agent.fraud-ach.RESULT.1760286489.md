```json
{
  "id": "b5fa1f569b9657e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286489,
  "host_pid": "9e6742732c60:1",
  "hash": "ac84686d784dd2b9a9d4a957525ed6d03406610f68b4f522aaced89d38d5633e",
  "cid": "QmV1ac84686d784dd2b9a9d4a957525ed6d03406610f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286489,
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
      "evaluated_at": 1760286489
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "4127bacf11b6fd0788a56dfb08d150dffe0d2b75281d994796d16e5f631c43da"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105154361187
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285764, 'matching_hash': 'a57b8c5e7960514a'}}}re': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285764, 'matching_hash': 'ca8349fc21f82b4d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6888614}}}