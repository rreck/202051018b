```json
{
  "id": "45815aab5f8e22ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286700,
  "host_pid": "9e6742732c60:1",
  "hash": "a381e9bddcddc7dae987cd3f7885b0982a5d37825a20079c4fff1d9ad9d38833",
  "cid": "QmV1a381e9bddcddc7dae987cd3f7885b0982a5d3782",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286700,
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
      "evaluated_at": 1760286700
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
  "sig": "09a3d7fba65fca7a417d3fd1b469f6908f09ee3f544aef8b48d32b523e65788d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462119178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14398286, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': '2f807700ebd65d7c'}}}