```json
{
  "id": "992d1ef5eb38afba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286224,
  "host_pid": "9e6742732c60:1",
  "hash": "c5cccb75f7bfeacc40f9fe90d2c4945ca096c23c51afbcfc5f711aa6417cb522",
  "cid": "QmV1c5cccb75f7bfeacc40f9fe90d2c4945ca096c23c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286224,
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
      "evaluated_at": 1760286224
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
  "sig": "73235d861d4b6dfe890d528cb4ae612cdeaeb1a8c765332e8a25ad4232c40631"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242521033
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}