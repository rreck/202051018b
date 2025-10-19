```json
{
  "id": "9f97836d31c07e96",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285442,
  "host_pid": "9e6742732c60:1",
  "hash": "a4012d5a3b0be3cb3f4c502d4f37113ad329e5f41b1bd303f4985e1f135b3802",
  "cid": "QmV1a4012d5a3b0be3cb3f4c502d4f37113ad329e5f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285442,
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
      "evaluated_at": 1760285442
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
  "sig": "9afb551f985f8fe6a45d0cb771cb752020a64a4dc62271b610a958cad5f5797e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 19384124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}