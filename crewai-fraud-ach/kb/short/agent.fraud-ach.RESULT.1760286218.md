```json
{
  "id": "f6327e3722749785",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286218,
  "host_pid": "9e6742732c60:1",
  "hash": "24d59f0c212848a53b4c1fd3e1dd918e70e523808b74900e32de986d2ce47407",
  "cid": "QmV124d59f0c212848a53b4c1fd3e1dd918e70e52380",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286218,
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
      "evaluated_at": 1760286218
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
  "sig": "076f169ee32405a17d92a78584d2fb8a8d8665b18d902f093899436b6ffc3f81"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243277611
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}