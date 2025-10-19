```json
{
  "id": "9c0b60ba66ef0f40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287246,
  "host_pid": "9e6742732c60:1",
  "hash": "e981ad66727306ab71aa15cdbb8fd5f0433a7f52fa4ec316ff89fa6eb830d9da",
  "cid": "QmV1e981ad66727306ab71aa15cdbb8fd5f0433a7f52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287246,
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
      "evaluated_at": 1760287246
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
  "sig": "ed3d1ff126947a09a9ba7d9609d965bf4395c25b7d97e9e8a92074a3e893670a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462505262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 20751302, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285764, 'matching_hash': 'e15f6eb56271d036'}}}