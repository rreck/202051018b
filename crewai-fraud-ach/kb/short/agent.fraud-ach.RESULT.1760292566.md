```json
{
  "id": "f1aee4424222a5d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292566,
  "host_pid": "9e6742732c60:1",
  "hash": "ddc2286492bc7f21dd8b2f9be6ac221684eaff4c7df881e663281dc5416d9de9",
  "cid": "QmV1ddc2286492bc7f21dd8b2f9be6ac221684eaff4c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292566,
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
      "evaluated_at": 1760292566
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
  "sig": "93598eebc8e5cd49408d47835907214efdffb8504cfa82b8294c65be94bf5315"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038607326
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 31785200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '23e85c6499cf881c'}}}