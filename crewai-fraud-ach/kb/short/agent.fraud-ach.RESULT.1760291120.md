```json
{
  "id": "9dcb0fd1d3808f4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291120,
  "host_pid": "9e6742732c60:1",
  "hash": "5df5af628c52135ccbe8b40c7a8ddc7b771908969deb4f93400fb575bab44f81",
  "cid": "QmV15df5af628c52135ccbe8b40c7a8ddc7b77190896",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291120,
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
      "evaluated_at": 1760291120
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
  "sig": "b584064c5e91507b906c045bf0d091ee85bdfe984b977f67b6a5cc317cf254d7"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 063100278543685
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 1183922786, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285765, 'matching_hash': 'e9470cd0cc07fb40'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.62, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7089358}}}