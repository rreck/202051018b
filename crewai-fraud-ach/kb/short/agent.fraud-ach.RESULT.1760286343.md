```json
{
  "id": "4bf5c1c8a7715ef4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286343,
  "host_pid": "9e6742732c60:1",
  "hash": "be78eddbde934c3127a4c09975bacaa21fd04464e3e24de741d892787d669674",
  "cid": "QmV1be78eddbde934c3127a4c09975bacaa21fd04464",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286343,
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
      "evaluated_at": 1760286343
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
  "sig": "229ad0e3bc8b449f6c8062cbb9ec1c2f0d22c15844fa140af99aaeee618ddbce"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039663431
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285764, 'matching_hash': '33f644fe289ea89d'}}}