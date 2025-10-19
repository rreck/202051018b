```json
{
  "id": "ec622edeadae03e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294715,
  "host_pid": "9e6742732c60:1",
  "hash": "b6d71ad8dc9d5369d86b5b2353e6930dc906d984631efdad0a03709ff46de8c9",
  "cid": "QmV1b6d71ad8dc9d5369d86b5b2353e6930dc906d984",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294715,
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
      "evaluated_at": 1760294715
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
  "sig": "f6921f7d61b4ea9f94b4b339a4583b8866cbd72bee80fe1da46cbe6011e66a2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028475138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 80773200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': 'fd3dd6a8db70ef91'}}}