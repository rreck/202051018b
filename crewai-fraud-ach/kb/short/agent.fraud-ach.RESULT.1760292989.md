```json
{
  "id": "db2d506511965d64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292989,
  "host_pid": "9e6742732c60:1",
  "hash": "3da5abc7383343eb4f62e70e5f22e257907f4d04e60ace5eeae944855cc4e408",
  "cid": "QmV13da5abc7383343eb4f62e70e5f22e257907f4d04",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292989,
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
      "evaluated_at": 1760292989
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
  "sig": "6eab61ea0e7325a9c51eb6bda794bb871979140c28ecf20637391989832856c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272135261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 285, 'threshold': 50, 'total_amount': 91013040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 284, 'first_seen': 1760284979, 'matching_hash': 'c71937e0bf846771'}}}}