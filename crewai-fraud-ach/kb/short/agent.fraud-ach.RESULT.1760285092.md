```json
{
  "id": "b316a3e0bc92ee15",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285092,
  "host_pid": "9e6742732c60:1",
  "hash": "70f4685ee45dcd61adc93e704ff8694ed2570e8a737190330a76bbad9a5e5ac1",
  "cid": "QmV170f4685ee45dcd61adc93e704ff8694ed2570e8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285092,
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
      "evaluated_at": 1760285092
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
  "sig": "6ca621e3f6ff954d8b5d690ba7c61c2d2a4d37303a90f5a92b41f6a8f59d68d1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}