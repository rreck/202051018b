```json
{
  "id": "d095305d8e58a5c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292545,
  "host_pid": "9e6742732c60:1",
  "hash": "6477f4960d44093c92c8ad7cf601c9b1daf6f1f5e4d2fc8c1d410c1c54a2a7a9",
  "cid": "QmV16477f4960d44093c92c8ad7cf601c9b1daf6f1f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292545,
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
      "evaluated_at": 1760292545
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
  "sig": "8e21d366e24d313397ed058397802e096b93e93528562a0810f6aeed752b2d25"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464121559
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 90758600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '1ddc8562b5a9ecf0'}}}