```json
{
  "id": "f233216d95356d22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292429,
  "host_pid": "9e6742732c60:1",
  "hash": "e67ea317fe73f7858d4665a1492a4e24469bb9f6ab2d898ed2c72f7b76c9c92d",
  "cid": "QmV1e67ea317fe73f7858d4665a1492a4e24469bb9f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292429,
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
      "evaluated_at": 1760292429
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
  "sig": "a4f4e0136b7c02639208d6071a4fbad3196b8da74dda84ef64d54be764c0f36a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036717829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 34029583, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285764, 'matching_hash': '49d069f76f563267'}}}