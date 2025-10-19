```json
{
  "id": "bb5f4573f9d0caa1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286087,
  "host_pid": "9e6742732c60:1",
  "hash": "e535202e8a8a31f6e42c196840484462e90db28bc005e7c3f94b642f6be9c70a",
  "cid": "QmV1e535202e8a8a31f6e42c196840484462e90db28b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286087,
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
      "evaluated_at": 1760286087
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
  "sig": "b37f48375947e07552eb8721b208b12f8932d0dcc5547e3d2dbfaaded61366c1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000027703590
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': '3a097b663e3dde58'}}}