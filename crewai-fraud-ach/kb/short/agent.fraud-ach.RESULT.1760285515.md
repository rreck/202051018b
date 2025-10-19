```json
{
  "id": "04f37149ebbe7181",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285515,
  "host_pid": "9e6742732c60:1",
  "hash": "08df08191a1948de1409abb8269783619ab8a6e5fda7f8453d5d2d1079c81fb7",
  "cid": "QmV108df08191a1948de1409abb8269783619ab8a6e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285515,
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
      "evaluated_at": 1760285515
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
  "sig": "ba4d76d1c0d936d393c58ad7696cb21d7c3be4ad1c1729b52f2e9dea2ce5f294"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 22333882, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}