```json
{
  "id": "b7e977c86ec7e0fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292232,
  "host_pid": "9e6742732c60:1",
  "hash": "e245d70f39182f16d4b4d2c99c1de93c7e1d49471321ab4d59e41dee0e7bfc65",
  "cid": "QmV1e245d70f39182f16d4b4d2c99c1de93c7e1d4947",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292232,
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
      "evaluated_at": 1760292232
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
  "sig": "be3feedacc28ec50935114c617804cf68adea41aabbb9b58e2a115999612d98a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156622392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 46405692, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '760602768636d516'}}}