```json
{
  "id": "acb257903926c4c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292131,
  "host_pid": "9e6742732c60:1",
  "hash": "985ab6b05224b715501cbb8e53b52ae5fef8fb0b206dbd0d34943448d562b920",
  "cid": "QmV1985ab6b05224b715501cbb8e53b52ae5fef8fb0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292131,
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
      "evaluated_at": 1760292131
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
  "sig": "5fb55706b93fb04b82c1e092eca05b33e67fbad016ca4e432dbc30e2f76f3e04"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278631812
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 36256002, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'e154fa328ed40444'}}}