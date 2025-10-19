```json
{
  "id": "00e43b498f441b33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285525,
  "host_pid": "9e6742732c60:1",
  "hash": "f13ae0f01aa4b13378b48d634b567b601eba8e4b9f1d91c02f46273cd0f273ce",
  "cid": "QmV1f13ae0f01aa4b13378b48d634b567b601eba8e4b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285525,
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
      "evaluated_at": 1760285525
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
  "sig": "4ff71d82e15093217c8c3fe6e64df0ff00a59f23af3f64ad8be59f0ca310d329"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 22755276, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}