```json
{
  "id": "ece3bd6961170ef4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294348,
  "host_pid": "9e6742732c60:1",
  "hash": "905d96182f1683db986a9aed21b32d05145d1baf3987585aee72f3fd39ae8dbb",
  "cid": "QmV1905d96182f1683db986a9aed21b32d05145d1baf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294348,
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
      "evaluated_at": 1760294348
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
  "sig": "eb203c9cf172f9826ad7fe2e2e0437c89ff3ccfaf8fe5d6be31de481d97f7954"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249127775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 33947184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '35c1bd481e0f1f5f'}}}