```json
{
  "id": "53bc7a590ef9efb9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294195,
  "host_pid": "9e6742732c60:1",
  "hash": "a52cff01542539f841466d731074a6910e56924d0b08490f0ef072661e7df077",
  "cid": "QmV1a52cff01542539f841466d731074a6910e56924d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294195,
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
      "evaluated_at": 1760294195
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
  "sig": "617a950f0e7355b4270572c9d44d2366d4af7f4791c61fbee5e84a88d126d454"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279407211
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 50664685, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': 'efd9a787beb40cb2'}}}