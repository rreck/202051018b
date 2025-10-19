```json
{
  "id": "55f659e85a0d89bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292105,
  "host_pid": "9e6742732c60:1",
  "hash": "84302e783246a1f445a532bd2e44d44c023d568f529f0fe4319ed5ac3318783b",
  "cid": "QmV184302e783246a1f445a532bd2e44d44c023d568f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292105,
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
      "evaluated_at": 1760292105
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
  "sig": "e1de11b1dfb1b56ab430d82b39ba99952eeeb2c4935a5bd950d9680a2d41a3b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 266, 'threshold': 50, 'total_amount': 112090804, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 265, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}aly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.96, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7672042}}}