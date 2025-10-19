```json
{
  "id": "1c5a03cc7e37a47a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287023,
  "host_pid": "9e6742732c60:1",
  "hash": "498bb21bf10f052cc31d1d2c2eb54f3a23826316d2fbd331712c1a0335646a99",
  "cid": "QmV1498bb21bf10f052cc31d1d2c2eb54f3a23826316",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287023,
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
      "evaluated_at": 1760287023
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
  "sig": "d83f936b544ac72040dc5f8234c3df2730d19c41efa577845163e8a37809cdde"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201466702370
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285765, 'matching_hash': 'c2e86be7e57e9a06'}}}