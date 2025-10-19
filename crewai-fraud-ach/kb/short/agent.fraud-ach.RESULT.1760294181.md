```json
{
  "id": "cc3b8fa90490fa9e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294181,
  "host_pid": "9e6742732c60:1",
  "hash": "0106e74ecf98a22c2fa40d03ee782cb8c94d19a3ef035af989f6af47dcf5e11b",
  "cid": "QmV10106e74ecf98a22c2fa40d03ee782cb8c94d19a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294181,
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
      "evaluated_at": 1760294181
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
  "sig": "608d040b1e43b6c84c8cb8894fb3f0b5c1fe54ae64e425b30ca43c4d95d3c144"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025069817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 110733017, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '107b8433ca6199ca'}}}