```json
{
  "id": "4be202cdd674fec3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291116,
  "host_pid": "9e6742732c60:1",
  "hash": "3304559c1132125cc7c4f3e284e08eb631befdb5cb45a6aad3361f7623ccd533",
  "cid": "QmV13304559c1132125cc7c4f3e284e08eb631befdb5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291116,
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
      "evaluated_at": 1760291116
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
  "sig": "917c16ab4d7881c9b9d26a661325ce321870595ab47c64890fbe8f5593d818cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028366239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 22732374, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': 'fc3cc28fddce4cc6'}}}