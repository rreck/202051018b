```json
{
  "id": "262bb6a7bc93bb86",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289800,
  "host_pid": "9e6742732c60:1",
  "hash": "8987cc83e4ef1b0afcb06a5fa6f9e6b708c153634d7f5b8840a0fcc487f4a599",
  "cid": "QmV18987cc83e4ef1b0afcb06a5fa6f9e6b708c15363",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289800,
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
      "evaluated_at": 1760289800
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
  "sig": "3f5d8b4c6f8896d1e7baa5532b74bbf0f01b886dd815da1e1b699df2975f92a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248025724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 15079274, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285764, 'matching_hash': 'cc12810353983743'}}}