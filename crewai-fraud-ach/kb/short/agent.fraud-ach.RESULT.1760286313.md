```json
{
  "id": "3bcda0cc4c9cb1ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286313,
  "host_pid": "9e6742732c60:1",
  "hash": "9fd8a17dae8b90cf55b6af7e089c6b3d2fe0817ca5f0f554ad70564d13a3974d",
  "cid": "QmV19fd8a17dae8b90cf55b6af7e089c6b3d2fe0817c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286313,
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
      "evaluated_at": 1760286313
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
  "sig": "3b4921bf715f7bd9b5c593a0815c861419b2a4c26fcaf30e9a1c7aa904905be6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105151422831
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285764, 'matching_hash': 'e9fc645b92693d6a'}}}