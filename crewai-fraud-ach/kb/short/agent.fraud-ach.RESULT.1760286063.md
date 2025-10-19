```json
{
  "id": "d1bb23265813602f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286063,
  "host_pid": "9e6742732c60:1",
  "hash": "377d57fe67d3b9d0c9366c8be7cc07da51d828e1bed9068d73201f19741982be",
  "cid": "QmV1377d57fe67d3b9d0c9366c8be7cc07da51d828e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286063,
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
      "evaluated_at": 1760286063
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
  "sig": "13263d09191af418f681c6f48016776217c8d06f29a2ca25b8ee2a4b9b10f48e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270130572
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285763, 'matching_hash': '3a095194dc4eaf85'}}}