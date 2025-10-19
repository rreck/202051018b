```json
{
  "id": "b7d1115010317a43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286984,
  "host_pid": "9e6742732c60:1",
  "hash": "87d0cbcb6820e41398a94ac0d0353d8899d708feaf651ceb69727fabccc3754b",
  "cid": "QmV187d0cbcb6820e41398a94ac0d0353d8899d708fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286984,
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
      "evaluated_at": 1760286984
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
  "sig": "156688530a2b702db5943822a51831011a01766296ad81dbc18696d468ae3cb5"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100276997857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20932868, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': 'b73e9a6de72cc131'}}}