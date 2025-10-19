```json
{
  "id": "43d5341ee8c65731",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287216,
  "host_pid": "9e6742732c60:1",
  "hash": "7434713d7ce4c02e45b3a821a310d1067d7977f2e1d8cf0bc5087d638ed356e3",
  "cid": "QmV17434713d7ce4c02e45b3a821a310d1067d7977f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287216,
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
      "evaluated_at": 1760287216
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "7b85d68da846b2d932c062dcb567f4d510fb970b391ede33d5ef144d8d2ff98e"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 121000242202372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 484810924, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285763, 'matching_hash': '7eed822364ae6d91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.54, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9323287}}}