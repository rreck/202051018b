```json
{
  "id": "8f6c48782827fbe0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292415,
  "host_pid": "9e6742732c60:1",
  "hash": "a352778718d432e681d718e259a39e8a46bac977a06c354720551125758d925b",
  "cid": "QmV1a352778718d432e681d718e259a39e8a46bac977",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292415,
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
      "evaluated_at": 1760292415
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
  "sig": "fb8f336125c6897ea19e94da73b33f519d929f82205a169b3028fa70a607ccb6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026876887
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 52569844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': 'ac27634a0ee0b6ee'}}}