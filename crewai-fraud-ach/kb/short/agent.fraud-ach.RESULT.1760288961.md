```json
{
  "id": "73c8652875494bc3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288961,
  "host_pid": "9e6742732c60:1",
  "hash": "837a61c706c7601f0b918307bdca124c1ac88aa065f6c49621074ed51c56c29f",
  "cid": "QmV1837a61c706c7601f0b918307bdca124c1ac88aa0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288961,
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
      "evaluated_at": 1760288961
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
  "sig": "5a4bcfa58f82e4e6738cd703a08293659535f158427b9ac1000c426b167c08fe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469922578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 13375935, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': '96901979868c282a'}}}