```json
{
  "id": "0c9ef5b1495e4fdf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286156,
  "host_pid": "9e6742732c60:1",
  "hash": "d0491e71764335cf179dc467be8a04710429420e695c8d17e658d2d550e519d5",
  "cid": "QmV1d0491e71764335cf179dc467be8a04710429420e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286156,
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
      "evaluated_at": 1760286156
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
  "sig": "3d5d877dc3dade65a2ff2bf5b5a989db7112cd7f5a9914a4816428a51767cc4e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243649474
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285763, 'matching_hash': '901672e1b111b3e4'}}}