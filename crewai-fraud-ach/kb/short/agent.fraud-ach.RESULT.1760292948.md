```json
{
  "id": "9a9b32d0e8f23e9e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292948,
  "host_pid": "9e6742732c60:1",
  "hash": "b3bda151a6bdfda595e989aad2c7acfb4aa736ef9c45f635ac961a6e2d0be047",
  "cid": "QmV1b3bda151a6bdfda595e989aad2c7acfb4aa736ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292948,
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
      "evaluated_at": 1760292948
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
  "sig": "92e48f9c429c50d453f44d1d98b95b2f62d364a15b62f06988dc736cc4c05892"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243187094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 93266160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285764, 'matching_hash': '46900333a68fa7ba'}}}