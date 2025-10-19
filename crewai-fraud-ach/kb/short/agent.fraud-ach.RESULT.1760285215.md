```json
{
  "id": "c6b5d6f20bdb534e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285215,
  "host_pid": "9e6742732c60:1",
  "hash": "384da79116a92813ebd69a3e129e95d21f5816f44d77e7af1a822c248465209f",
  "cid": "QmV1384da79116a92813ebd69a3e129e95d21f5816f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285215,
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
      "evaluated_at": 1760285215
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
  "sig": "a96c01289460f4ca9920697aac42e14a1a666f486b14133b1d0a129adafaf4b7"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10113456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}