```json
{
  "id": "a144b5650b75d83a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292092,
  "host_pid": "9e6742732c60:1",
  "hash": "da3863ff2e91ad288454ee04f0ec62c9aac44d98188310d6e2af5181b10c91b2",
  "cid": "QmV1da3863ff2e91ad288454ee04f0ec62c9aac44d98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292092,
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
      "evaluated_at": 1760292092
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
  "sig": "f04e66807ffe0fcb274b1f73a5d9ec193d18c36c29cac4d2e305f99da93a2151"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032147418
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 70501780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285764, 'matching_hash': '7eb9a0fe320f28ac'}}}