```json
{
  "id": "6358b25ace96a237",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290572,
  "host_pid": "9e6742732c60:1",
  "hash": "4e830751f2096466fa66bc780b015d6cf20f5833136159c267e2e7a9c190517b",
  "cid": "QmV14e830751f2096466fa66bc780b015d6cf20f5833",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290572,
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
      "evaluated_at": 1760290572
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
  "sig": "3a96c1a61cb28ad8cc0cf44f6ce61b948c887c78e233fba799e2fbc00ee117d9"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009592950397
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 1433226256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': '5b23ebe5172c1d5f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.89, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9306664}}}