```json
{
  "id": "83958e86e4d5acb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285462,
  "host_pid": "9e6742732c60:1",
  "hash": "1881a1989b62988bb6421b9f9b52a731598ad769f9f166e2c9cf3e8dbc638ba2",
  "cid": "QmV11881a1989b62988bb6421b9f9b52a731598ad769",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285462,
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
      "evaluated_at": 1760285462
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
  "sig": "be39634435ad7fa6079e3a999599cfa74eee7ff8f729a77785865baeb71c8272"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20226912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}