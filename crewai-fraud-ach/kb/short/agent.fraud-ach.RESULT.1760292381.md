```json
{
  "id": "d879e11969580470",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292381,
  "host_pid": "9e6742732c60:1",
  "hash": "f12f3aaed3a6da39bb6540e99385322d3d94a8c8b82bc14354c5d1bee40348ee",
  "cid": "QmV1f12f3aaed3a6da39bb6540e99385322d3d94a8c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292381,
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
      "evaluated_at": 1760292381
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
  "sig": "e918c23c2d732a487784646acc4e0a7e572d7fa51cac9610ffb252ec381376f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022841229
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 34920340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '5d206cfe266207b6'}}}