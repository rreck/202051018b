```json
{
  "id": "3a3dce80b9c4fd45",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288968,
  "host_pid": "9e6742732c60:1",
  "hash": "cbbea986dda9789d5f095c8493d7476f5b78da59154a861b1606a99d53a782c5",
  "cid": "QmV1cbbea986dda9789d5f095c8493d7476f5b78da59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288968,
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
      "evaluated_at": 1760288968
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
  "sig": "e2de672f1dced009f4a47f9313c93138b30fdcddab21cb5a98f5e5912f61e453"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 34068059, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}