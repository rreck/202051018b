```json
{
  "id": "d85edfe6ba83ff2b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292593,
  "host_pid": "9e6742732c60:1",
  "hash": "246a84cfe793bbe0549175d87622c08f3fa25cecf9a00311ff5f8c91935f1beb",
  "cid": "QmV1246a84cfe793bbe0549175d87622c08f3fa25cec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292593,
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
      "evaluated_at": 1760292593
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
  "sig": "6d8653167586d9f138c2a4a4390ff9628db198c9ffaa09b8da7539f2f227ee83"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246132965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 88377891, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': 'ed6ec2b6e100ea2c'}}}