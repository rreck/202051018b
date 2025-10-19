```json
{
  "id": "bdc5ea8dd2b8c807",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292519,
  "host_pid": "9e6742732c60:1",
  "hash": "4e490d86f0e2bd3aad1eccff05c1bb8371629cc2733f4eca37aa30ebf128860d",
  "cid": "QmV14e490d86f0e2bd3aad1eccff05c1bb8371629cc2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292519,
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
      "evaluated_at": 1760292519
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
  "sig": "1bb01aea65cb101ecda0d0c018cf0541e8899aeef6d393089ec5a152f04c52d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034053694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 10666798, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285765, 'matching_hash': 'f3f5d61420936f73'}}}