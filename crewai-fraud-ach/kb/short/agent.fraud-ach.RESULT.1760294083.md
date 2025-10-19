```json
{
  "id": "d2924e1412cbe51a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294083,
  "host_pid": "9e6742732c60:1",
  "hash": "11d68f8639e4b4dd27de6e4c7593f8335a4d9a5739586f59071ed1998678c6d7",
  "cid": "QmV111d68f8639e4b4dd27de6e4c7593f8335a4d9a57",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294083,
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
      "evaluated_at": 1760294084
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
  "sig": "1c36da9a416697b4816000750ed9ccb82a2aa36ebae4adc8f681a24ce717afdb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278613406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 95175234, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': 'bc206509fe1a9621'}}}