```json
{
  "id": "f42031f182f28b1a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290284,
  "host_pid": "9e6742732c60:1",
  "hash": "5a6758d7dae485d941411467900cd5f2d8d7be055740c8cfee8bbec1944aec41",
  "cid": "QmV15a6758d7dae485d941411467900cd5f2d8d7be05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290284,
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
      "evaluated_at": 1760290284
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
  "sig": "762241140c345969be679e7f47f94cb3394a747d6a034f5aab594ded399ddcba"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100279293429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 764933128, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': 'f44f07036b33cc03'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5239268}}}