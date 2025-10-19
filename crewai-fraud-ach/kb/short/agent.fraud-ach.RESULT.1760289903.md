```json
{
  "id": "ea8851693fd1f2e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289903,
  "host_pid": "9e6742732c60:1",
  "hash": "be45450480f47d31aa651baf55d61b63314da4cfe823cacccd5b9ffda2c73792",
  "cid": "QmV1be45450480f47d31aa651baf55d61b63314da4cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289903,
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
      "evaluated_at": 1760289903
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
  "sig": "23bc0038b65a69df1f20a99d0c4ae9770a8b569736a0f863a6cdcb7e36490068"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000021698868
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 1200563420, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760284979, 'matching_hash': '4224f1af7034834c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5663035}}}bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6131353}}}