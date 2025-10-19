```json
{
  "id": "c3efa459d9a6e412",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287548,
  "host_pid": "9e6742732c60:1",
  "hash": "b501f8ce04ec46f2be3014d867f14fc59d8577d3aafaa1667398e48cae68c62e",
  "cid": "QmV1b501f8ce04ec46f2be3014d867f14fc59d8577d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287548,
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
      "evaluated_at": 1760287548
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
  "sig": "806038f415f0e345ca865328878d53ef6c283c1973472cf41b53a5d46ca7dae9"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 121000241124617
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 17689728, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285763, 'matching_hash': 'fcf7fec38d983fba'}}}