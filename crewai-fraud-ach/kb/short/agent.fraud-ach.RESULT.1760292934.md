```json
{
  "id": "daa1ecd16b7fdea4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292934,
  "host_pid": "9e6742732c60:1",
  "hash": "0867ff267b9d104304f0454c321452f22d2de22c2b85dc5ac6c57af822384649",
  "cid": "QmV10867ff267b9d104304f0454c321452f22d2de22c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292934,
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
      "evaluated_at": 1760292934
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
  "sig": "9be8e03183df0636dae852df93897f15e467d03855f411418ad76ccbf05072a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023207579
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 74902464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': '07d0951e15487e7b'}}}