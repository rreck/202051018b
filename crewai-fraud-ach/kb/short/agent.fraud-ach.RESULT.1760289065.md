```json
{
  "id": "d5dae4c9b6634150",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289065,
  "host_pid": "9e6742732c60:1",
  "hash": "9041bb176c82cb83f965565b00ddb9fee12bb8df42924ac770ce61344d7bfc69",
  "cid": "QmV19041bb176c82cb83f965565b00ddb9fee12bb8df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289065,
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
      "evaluated_at": 1760289065
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
  "sig": "a1c2f16cdedad0cd0a7281f870aa52de82726fa3866088f59538d1cc9791176c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022218542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 45506608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285765, 'matching_hash': 'd495c26a449690da'}}}