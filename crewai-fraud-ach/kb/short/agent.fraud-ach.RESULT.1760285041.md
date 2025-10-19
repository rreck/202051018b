```json
{
  "id": "2a5d7c4e01d08a8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285041,
  "host_pid": "9e6742732c60:1",
  "hash": "599b86c7a0438096bcdf67d95e093617e7d82f090297075f0bf3b8120f033b0c",
  "cid": "QmV1599b86c7a0438096bcdf67d95e093617e7d82f09",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285041,
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
      "evaluated_at": 1760285041
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
  "sig": "9b9b26656a48303f40f9e05393f99f4c6aab4468d539c40a3b374b9420f7a317"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}