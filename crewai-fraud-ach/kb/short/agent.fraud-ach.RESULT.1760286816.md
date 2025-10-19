```json
{
  "id": "de703329f964e882",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286816,
  "host_pid": "9e6742732c60:1",
  "hash": "1b36fc2b7c783978f10e50c9382a18a775106f74b02cceacdafb9fb480ad87aa",
  "cid": "QmV11b36fc2b7c783978f10e50c9382a18a775106f74",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286816,
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
      "evaluated_at": 1760286816
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
  "sig": "007b3de51e3f1ff781d8010e488569542577311ae0f8999cea09c67cf0b66d6d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029578937
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285765, 'matching_hash': '7dfe5cbbd07b7822'}}}