```json
{
  "id": "b66325f8855f9704",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292811,
  "host_pid": "9e6742732c60:1",
  "hash": "6181a45df5ff364d6006fc2706a1f69d67490c477d47f590c98f03d1da887852",
  "cid": "QmV16181a45df5ff364d6006fc2706a1f69d67490c47",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292811,
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
      "evaluated_at": 1760292811
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
  "sig": "48caf703626d5b43ee3075c34fb8daac9f9025d0d421fef4fdfa2e23652deeaa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158656793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 62134270, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': 'b1ac6f9d66d66d2b'}}}