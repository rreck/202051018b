```json
{
  "id": "fe99c61df8d53880",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291293,
  "host_pid": "9e6742732c60:1",
  "hash": "a3fe4b173ef56f258d511c4d1ce9bb24869093ccbe6aa990be468be9c5b1607a",
  "cid": "QmV1a3fe4b173ef56f258d511c4d1ce9bb24869093cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291293,
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
      "evaluated_at": 1760291293
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
  "sig": "4314155702e9827607fb1ed45a3dd0a4c87d74d93cbebcf5f45bc942f4be1f48"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 54420408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}