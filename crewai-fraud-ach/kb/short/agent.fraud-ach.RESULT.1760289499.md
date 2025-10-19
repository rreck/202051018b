```json
{
  "id": "8fcb4a5e30f6406f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289499,
  "host_pid": "9e6742732c60:1",
  "hash": "269d7adcdba66d107e15b29dafa66d187182723a0a8712edee57fd8d06646b22",
  "cid": "QmV1269d7adcdba66d107e15b29dafa66d187182723a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289499,
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
      "evaluated_at": 1760289499
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
  "sig": "f3dae9a120f7cad1b52b1076253fd14013d204a5ac25ef2be14a326ef1a23bb8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241053391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 53560375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '6e04470f15e4fc18'}}}