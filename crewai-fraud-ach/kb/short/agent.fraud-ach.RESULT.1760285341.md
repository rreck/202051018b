```json
{
  "id": "9489f8ce95690725",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285341,
  "host_pid": "9e6742732c60:1",
  "hash": "ff0c9fd778a3051481f1a135d27f86d0541acbd46f71fa7c0c59139b1a88e6e7",
  "cid": "QmV1ff0c9fd778a3051481f1a135d27f86d0541acbd4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285341,
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
      "evaluated_at": 1760285341
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "91cadf78046e7b9abe5742215e39e29f6abfbf065d3f3d59be3ebd1451248f35"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15170184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}