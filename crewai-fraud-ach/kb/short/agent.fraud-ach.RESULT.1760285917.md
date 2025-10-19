```json
{
  "id": "3f5e0515def03808",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285917,
  "host_pid": "9e6742732c60:1",
  "hash": "5fbcdfde511785633078769422b025d7bfb4779f8626a9a660e3418e93944da8",
  "cid": "QmV15fbcdfde511785633078769422b025d7bfb4779f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285917,
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
      "evaluated_at": 1760285917
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
  "sig": "b0fe8ba689728fdd473a4e30d0ba5af91c9f4cb992c5494062527b1950d35c00"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243890645
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285764, 'matching_hash': '25ed426365fec5d8'}}}