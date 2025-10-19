```json
{
  "id": "d7004e89e4ba1357",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287490,
  "host_pid": "9e6742732c60:1",
  "hash": "7658052795f77cff3cfade560382b93e47d89ed41361aad43fb64c2857fec5ee",
  "cid": "QmV17658052795f77cff3cfade560382b93e47d89ed4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287490,
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
      "evaluated_at": 1760287490
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
  "sig": "bb0d40b313358506db71a8d6502807ecb296027f08aabbeea78c1488e2a9fe67"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 121000248255202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 24994122, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285764, 'matching_hash': 'c66fc0c5e7caab92'}}}