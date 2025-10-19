```json
{
  "id": "419e19c89d93500f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287543,
  "host_pid": "9e6742732c60:1",
  "hash": "35adc78bc0b2967452596fa01026b1acad790cdbb9671b921f9c7fc743768084",
  "cid": "QmV135adc78bc0b2967452596fa01026b1acad790cdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287543,
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
      "evaluated_at": 1760287543
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
  "sig": "de8257bb9e19e1f88d9f1ef71d37bcf1dd85e8cccfe54ae91e72ffe6aae71be1"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 063100276193597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 16239360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285763, 'matching_hash': 'c482c58c8f3e1991'}}}