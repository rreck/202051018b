```json
{
  "id": "c5bf05a9d8a98b7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290504,
  "host_pid": "9e6742732c60:1",
  "hash": "93243ac8568a7cb27e4a1f02efac8c703384eeea0fa9caea37dde60b57a64409",
  "cid": "QmV193243ac8568a7cb27e4a1f02efac8c703384eeea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290504,
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
      "evaluated_at": 1760290504
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
  "sig": "c11834f5de80f22a06509e02c1afa27c4cc669f1bb8591955898fa686a168391"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038318648
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 48651856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': '13d51597e8ec53d0'}}}