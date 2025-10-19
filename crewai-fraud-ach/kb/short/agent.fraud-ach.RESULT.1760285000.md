```json
{
  "id": "318732b50ae7ed76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285000,
  "host_pid": "9e6742732c60:1",
  "hash": "b241b288e8b0eb5f6e71d849f1db442126d958a97b702b7dd85d4e55399dfbb3",
  "cid": "QmV1b241b288e8b0eb5f6e71d849f1db442126d958a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285000,
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
      "evaluated_at": 1760285000
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
  "sig": "94e4b54a55cee57c6efc527147cfa9e68b0c9292291162f775720776aa227814"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}