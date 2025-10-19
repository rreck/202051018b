```json
{
  "id": "2abb81d93b6aca89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286128,
  "host_pid": "9e6742732c60:1",
  "hash": "36689b4de86567ee6cc7261a65e9fe599bd0fa9cea34556725239897353f89a9",
  "cid": "QmV136689b4de86567ee6cc7261a65e9fe599bd0fa9c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286128,
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
      "evaluated_at": 1760286128
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
  "sig": "eba27c9a61f0f786d096161c329fcda1b9ffb37098c10cf76f6bdb4b597193f6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243277611
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}