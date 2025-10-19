```json
{
  "id": "cfee44c4e56ad8c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285640,
  "host_pid": "9e6742732c60:1",
  "hash": "03ce525503ea1f7a2bc04a81f489286e1d7df5f7501fccd130e368dd42550090",
  "cid": "QmV103ce525503ea1f7a2bc04a81f489286e1d7df5f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285640,
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
      "evaluated_at": 1760285640
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
  "sig": "e7faf7f7f83a5f69c92aa8ecf6e0cf2e4ef2da0d586b2f15b234026db1c1394d"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 27390610, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}