```json
{
  "id": "6af2666d6de2c618",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291887,
  "host_pid": "9e6742732c60:1",
  "hash": "dbdd0ede7dc70e09199e66065eefddcf7b235414ab2dc45a9d6c004b33c5510c",
  "cid": "QmV1dbdd0ede7dc70e09199e66065eefddcf7b235414",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291887,
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
      "evaluated_at": 1760291887
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "b6989bbeeeb43f907ee86b4ae1732245ec0a2d195f6738c5f954ebe801c668fa"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100275328879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 1036874310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285764, 'matching_hash': '9f5415d10b328afc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5604726}}}