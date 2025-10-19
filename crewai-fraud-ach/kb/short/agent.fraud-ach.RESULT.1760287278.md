```json
{
  "id": "e0a5bcd4918780c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287278,
  "host_pid": "9e6742732c60:1",
  "hash": "240f432240ed9ddb0f817bbd4f999ad93cf3970616a5a969afcc3ca346b2280d",
  "cid": "QmV1240f432240ed9ddb0f817bbd4f999ad93cf39706",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287278,
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
      "evaluated_at": 1760287278
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "894e8c9e891194deab242bb00d7fd1a2db044ec43f23c87d880a4bf37a803841"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105150171825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 10150326, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285765, 'matching_hash': 'da3473f59eec3040'}}}