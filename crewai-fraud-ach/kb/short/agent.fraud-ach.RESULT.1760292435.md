```json
{
  "id": "dea0708a505c66bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292435,
  "host_pid": "9e6742732c60:1",
  "hash": "a2e060dc24de67bbf0f0f4ec6931714249ad3210df6d5b68d4b926f27cacb40b",
  "cid": "QmV1a2e060dc24de67bbf0f0f4ec6931714249ad3210",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292435,
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
      "evaluated_at": 1760292435
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
  "sig": "d6376c827d1877d0eab0357b402f2655adb580d684a53a28803534d203cb367d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022135017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 14689699, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': 'ca41710ea386559e'}}}