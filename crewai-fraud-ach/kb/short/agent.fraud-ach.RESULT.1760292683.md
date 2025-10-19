```json
{
  "id": "a97f04ab6e51a63e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292683,
  "host_pid": "9e6742732c60:1",
  "hash": "ebe05cb8a6f9b7ad56f32aabb5d6261f84d0efc1a6d830e78ac17525c6d90de9",
  "cid": "QmV1ebe05cb8a6f9b7ad56f32aabb5d6261f84d0efc1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292683,
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
      "evaluated_at": 1760292683
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
  "sig": "585cdd8b4aec665a41dafab97a3f7ec9741dd7da99dc59b2cd51373bf5ef8c32"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467455813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 13769490, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': 'dd25b8ab6718ff18'}}}