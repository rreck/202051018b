```json
{
  "id": "801731d7ca25492e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291261,
  "host_pid": "9e6742732c60:1",
  "hash": "cc89655ec9d7396ce34872d0cf1ae98a6292f12a4fc76d22767dd01b0dfb7886",
  "cid": "QmV1cc89655ec9d7396ce34872d0cf1ae98a6292f12a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291261,
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
      "evaluated_at": 1760291261
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
  "sig": "89218f231f598913f32c4ce7e3516d1e5c015d42206b85dc791e2fe33a7b9654"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275498951
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 32521293, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': 'a1e1622f9da312c5'}}}