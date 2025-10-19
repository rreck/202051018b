```json
{
  "id": "cdb02f216fbf7e20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290122,
  "host_pid": "9e6742732c60:1",
  "hash": "6b8f4f5a555cfb2d904bf1a8a885067ed7c67a7b36c5e1fbc2aa306cdd055f1a",
  "cid": "QmV16b8f4f5a555cfb2d904bf1a8a885067ed7c67a7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290122,
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
      "evaluated_at": 1760290122
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
  "sig": "10f291ad361378399d6f46fddc43f43e4e80da130b914d32f6202131ebcc997f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466771941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 52254438, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': 'aa929aac6878f78f'}}}