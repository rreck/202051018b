```json
{
  "id": "93c1ceb12879ddc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294091,
  "host_pid": "9e6742732c60:1",
  "hash": "db2aea3c86802dd4578e055b7f5dbc77d43d31c15b4e22fd010a6959a8db5307",
  "cid": "QmV1db2aea3c86802dd4578e055b7f5dbc77d43d31c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294091,
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
      "evaluated_at": 1760294091
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
  "sig": "b2da4f7c3529fde1b918827bd2516fdd70e75104e167b2d271ba928f93b6bd2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025723119
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 108934749, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285764, 'matching_hash': '7f709c8256c8a242'}}}