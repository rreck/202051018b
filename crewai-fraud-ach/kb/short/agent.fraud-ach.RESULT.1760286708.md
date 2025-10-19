```json
{
  "id": "658f5a38ceb3ac1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286708,
  "host_pid": "9e6742732c60:1",
  "hash": "ce365fc5f5e710b9cb7c7fd2ef908b628eb2ab8cf26ec7639d6eabbd41fc434f",
  "cid": "QmV1ce365fc5f5e710b9cb7c7fd2ef908b628eb2ab8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286708,
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
      "evaluated_at": 1760286708
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "54ac6cd4d206f2102fb98f2c0e779a4d1b173b4d627583fc946bf3594a2e85b5"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105152525323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12513496, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285765, 'matching_hash': '867ad08c0d495d7b'}}}