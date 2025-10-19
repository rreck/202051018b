```json
{
  "id": "f0e75528d1950874",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289871,
  "host_pid": "9e6742732c60:1",
  "hash": "7f1dfc9651027f8a1289f2c6696bdcc993dd6a1e8e4614076b91a7decd34bb43",
  "cid": "QmV17f1dfc9651027f8a1289f2c6696bdcc993dd6a1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289871,
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
      "evaluated_at": 1760289871
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
  "sig": "610eb4c1c37cc48906e792d92bb1d3ea02cf5963119d5017fcb97c8d2b11f7ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 58175145, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}