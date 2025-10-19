```json
{
  "id": "8c2f7ff5eaf5d83e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286249,
  "host_pid": "9e6742732c60:1",
  "hash": "4d48f32629c3c98521696b99a52f6e50a1ac1b3fd262e70164ae4b423eb2c99b",
  "cid": "QmV14d48f32629c3c98521696b99a52f6e50a1ac1b3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286249,
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
      "evaluated_at": 1760286249
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
  "sig": "4150330073e41373bd3fbd55b3e78a1a3ae73234061dd762242d5dd4f4b391a4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100279407211
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285764, 'matching_hash': 'efd9a787beb40cb2'}}}