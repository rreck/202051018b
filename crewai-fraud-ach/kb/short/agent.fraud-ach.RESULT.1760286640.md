```json
{
  "id": "e842f4d4b2c6c959",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286640,
  "host_pid": "9e6742732c60:1",
  "hash": "8569bb38d704871391e1c2c8d8e6d1a032ed9966bf3d08f5ac5a4961fee21383",
  "cid": "QmV18569bb38d704871391e1c2c8d8e6d1a032ed9966",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286640,
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
      "evaluated_at": 1760286640
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
  "sig": "e51dd3cd2dfc6e8a0618bc4bc7b274b61042860a69148d938e0fcffee911e352"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022844283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 20344500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760284979, 'matching_hash': '9c963f39e9fb9122'}}}