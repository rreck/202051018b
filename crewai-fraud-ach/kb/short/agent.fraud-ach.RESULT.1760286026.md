```json
{
  "id": "d6038fe88d93cdb8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286026,
  "host_pid": "9e6742732c60:1",
  "hash": "7186d0dafde4da9379209dc1408d7759f8b89270ab7443761ca22dce567d79b3",
  "cid": "QmV17186d0dafde4da9379209dc1408d7759f8b89270",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286026,
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
      "evaluated_at": 1760286026
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
  "sig": "d11b352da66c17b2423bbb8dc59c454623bb87aa6060ff6ccc2afde80fd7239b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270133099
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285763, 'matching_hash': '05f0f8ce03828c9b'}}}