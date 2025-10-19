```json
{
  "id": "849c1b0cab542527",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287092,
  "host_pid": "9e6742732c60:1",
  "hash": "b2d57c728b4104a518d03a8a07c186b3ec5f481ed2b08e0f5afb8540c258bfdb",
  "cid": "QmV1b2d57c728b4104a518d03a8a07c186b3ec5f481e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287092,
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
      "evaluated_at": 1760287092
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
  "sig": "314dc02f2d7b09e7562da1960eb61eb91d8cf9f29453e359fefabfc03331954a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241272290
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285763, 'matching_hash': 'ac7868cb6249fe41'}}}