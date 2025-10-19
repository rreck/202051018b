```json
{
  "id": "75191f467755e8b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286709,
  "host_pid": "9e6742732c60:1",
  "hash": "f2ae46129a8e61a1425c058488cb883aefe26f8fd5e8be74eeee8ec74de4d4ce",
  "cid": "QmV1f2ae46129a8e61a1425c058488cb883aefe26f8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286709,
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
      "evaluated_at": 1760286709
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
  "sig": "b313ef4791a8dd3179fa18060962f969667173e20d80e7d1168e4bd7d50030a6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249334487
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}