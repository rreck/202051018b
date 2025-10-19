```json
{
  "id": "c079891d2535c4fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285392,
  "host_pid": "9e6742732c60:1",
  "hash": "2a436cf55a38b9e1b5d1c32e9c9c48764d5e821453dbc88e2086ee9f24047fc6",
  "cid": "QmV12a436cf55a38b9e1b5d1c32e9c9c48764d5e8214",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285392,
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
      "evaluated_at": 1760285392
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
  "sig": "0b029f794a880e796894c2b2edfba2510b20552c687d5bb333d7b2df6a44e578"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17277154, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}