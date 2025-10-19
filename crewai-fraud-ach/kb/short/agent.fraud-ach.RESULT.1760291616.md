```json
{
  "id": "aca2ff2583509a0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291616,
  "host_pid": "9e6742732c60:1",
  "hash": "da86b4bdb86bb8bd9f046228cea97129d96528d2e201628349f10a576088e9f3",
  "cid": "QmV1da86b4bdb86bb8bd9f046228cea97129d96528d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291616,
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
      "evaluated_at": 1760291616
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
  "sig": "5c6742edb115f31ae8ec57149e5e7ae4d727bd67d34662e9336423279a7ecafb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277305476
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 73041845, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'e8a0d4fc67d0b61c'}}}