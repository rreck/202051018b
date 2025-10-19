```json
{
  "id": "b8e3ea2877fc074a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286903,
  "host_pid": "9e6742732c60:1",
  "hash": "43043f3a3de3b1b9d869bf41d3836161acebb49ff0408ab8c5ba4fe065ef335e",
  "cid": "QmV143043f3a3de3b1b9d869bf41d3836161acebb49f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286903,
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
      "evaluated_at": 1760286903
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
  "sig": "dabf38c084ea6ddea4844eb4ef1cbb992cbe00b5a85052083942281a9a8b7730"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100279407211
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285764, 'matching_hash': 'efd9a787beb40cb2'}}}