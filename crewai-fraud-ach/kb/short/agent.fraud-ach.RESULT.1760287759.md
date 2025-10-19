```json
{
  "id": "189ff970d7c7a414",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287759,
  "host_pid": "9e6742732c60:1",
  "hash": "634458e8f7bc9b50a91b88f66710f2d551aa14149585a243d72272f0c72a8d1e",
  "cid": "QmV1634458e8f7bc9b50a91b88f66710f2d551aa1414",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287759,
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
      "evaluated_at": 1760287759
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
  "sig": "f8a2275a6fbf5d1fcc592043781a2379cf58ec62c5560831ccb6e99c34799a01"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 122105154024479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 22641971, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285765, 'matching_hash': 'af946edf21c4a5d6'}}}