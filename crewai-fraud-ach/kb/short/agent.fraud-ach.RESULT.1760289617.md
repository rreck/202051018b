```json
{
  "id": "822b3bbf2cfa795b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289617,
  "host_pid": "9e6742732c60:1",
  "hash": "5477f6eb5eef09817a508328eb763642e899ba2e43246495e0f2b5df0648e77d",
  "cid": "QmV15477f6eb5eef09817a508328eb763642e899ba2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289617,
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
      "evaluated_at": 1760289617
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
  "sig": "91127f8a3e1df98472ad5e227991a682a8d77c5377e55dd3c23076a6024712a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246932907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 57852928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': 'b5767c7cd6e7c742'}}}