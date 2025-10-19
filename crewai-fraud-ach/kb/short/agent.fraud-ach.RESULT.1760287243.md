```json
{
  "id": "7abc3237eb2ca761",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287243,
  "host_pid": "9e6742732c60:1",
  "hash": "bedba33d0cf7b834768e9860a294f2c66b5e751372ea8b326e377d7f9158eb28",
  "cid": "QmV1bedba33d0cf7b834768e9860a294f2c66b5e7513",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287243,
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
      "evaluated_at": 1760287243
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
  "sig": "702aa75071aec3cbb90f41757820473b6fc2ad9dc35ad6bd3bdc03c58f18ce61"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 15729605, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}