```json
{
  "id": "c07b8bbf34423e0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289374,
  "host_pid": "9e6742732c60:1",
  "hash": "68099d5b4e5e3b1ca9bf7fc2ca576148870b59455677a6a8c480e285422d6225",
  "cid": "QmV168099d5b4e5e3b1ca9bf7fc2ca576148870b5945",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289374,
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
      "evaluated_at": 1760289374
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
  "sig": "e7b5da6b337906a4a6683f86d6c35dd6105aabe9eb31f2b4eb2546e1479f90d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024109289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 42273649, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285765, 'matching_hash': 'ac2c8f9ff893d8ff'}}}