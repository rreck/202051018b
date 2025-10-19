```json
{
  "id": "e7c23f77f543e565",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288433,
  "host_pid": "9e6742732c60:1",
  "hash": "b79c75bd5cb3486c12a2ec0417609fdb67aec7dd3c7a50b57177f662c9b2bf1d",
  "cid": "QmV1b79c75bd5cb3486c12a2ec0417609fdb67aec7dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288433,
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
      "evaluated_at": 1760288433
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
  "sig": "6d21499f4522c24d9a831e881b09d77a7f43e6db1638fbe634ebf6c5ccd05026"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596807926
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 30532644, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285763, 'matching_hash': 'efb59c040be3d116'}}}