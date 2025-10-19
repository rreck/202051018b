```json
{
  "id": "fddda2e5790b2ed3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294131,
  "host_pid": "9e6742732c60:1",
  "hash": "3385a4a42cf7a73b3598793514ceaa91ff545ce0cda7743b90e2749c6d46aecd",
  "cid": "QmV13385a4a42cf7a73b3598793514ceaa91ff545ce0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294131,
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
      "evaluated_at": 1760294131
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
  "sig": "4db817e6eb3f4bc550961531849e9f6f354826ad854af76d87179a088f5aed0f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270162443
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 115311424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'e637274c2d5e4084'}}}