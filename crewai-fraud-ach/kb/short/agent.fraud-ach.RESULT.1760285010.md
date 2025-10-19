```json
{
  "id": "01947dadf47b2eb2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285010,
  "host_pid": "9e6742732c60:1",
  "hash": "d4e040e372d4d09891e14fc6e5e2b6701ceb869a1a21b8c58e56e8bfac21f2b3",
  "cid": "QmV1d4e040e372d4d09891e14fc6e5e2b6701ceb869a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285010,
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
      "evaluated_at": 1760285010
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
  "sig": "31933cea43de732b0bf971cc3ba52bc945aea234bd40ac56710d27ad06759084"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}