```json
{
  "id": "b6fd5812eed1d16e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285113,
  "host_pid": "9e6742732c60:1",
  "hash": "fb5fb4cf823daf9a17634aa2c914676a05a5592c65c9a17ca818541d144bc896",
  "cid": "QmV1fb5fb4cf823daf9a17634aa2c914676a05a5592c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285113,
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
      "evaluated_at": 1760285113
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
  "sig": "1c9243ff68a16b5d26ad142a1fcee98c7f0e775b57dcaba4482cb2d80a974e79"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}