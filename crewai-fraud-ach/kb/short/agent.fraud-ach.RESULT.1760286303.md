```json
{
  "id": "b849d9e30454c2ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286303,
  "host_pid": "9e6742732c60:1",
  "hash": "e8b19b1c21515ec235eb98a1dfb0a0ca5e51c0550d217020cb53ee3a9be2e5ca",
  "cid": "QmV1e8b19b1c21515ec235eb98a1dfb0a0ca5e51c055",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286303,
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
      "evaluated_at": 1760286303
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
  "sig": "c8983cf68568722451307fcac09ce75adbd11e92a3252d46271e64ca82a8b142"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009593654177
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285764, 'matching_hash': '5fbc310f1a1fe9dc'}}}