```json
{
  "id": "2e53671c4fb8b996",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291413,
  "host_pid": "9e6742732c60:1",
  "hash": "87475e16d80f17d24a0aeb9d2c5b7c9dd7db30d7dd69c98372aebad21eb8c40f",
  "cid": "QmV187475e16d80f17d24a0aeb9d2c5b7c9dd7db30d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291413,
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
      "evaluated_at": 1760291413
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
  "sig": "1c72e58beba3a221a09ba3152f0b12d090d4c90eb3d1ebbafb25b0798aba107b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460501611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 29512314, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285764, 'matching_hash': 'a26573d157351ea4'}}}