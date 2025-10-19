```json
{
  "id": "ce0797f37e2bc0b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288345,
  "host_pid": "9e6742732c60:1",
  "hash": "59519e1cb34ea8299ea09b6857f3d64493cbb6c40d9f85f3da595801398fb6aa",
  "cid": "QmV159519e1cb34ea8299ea09b6857f3d64493cbb6c4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288345,
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
      "evaluated_at": 1760288345
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
  "sig": "977cd26f05c89ea5548e5baa484d94d0b0441f8796eb9add3481152c71e1908e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038099532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 36127980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285765, 'matching_hash': 'ac68ba9e81a65c72'}}}