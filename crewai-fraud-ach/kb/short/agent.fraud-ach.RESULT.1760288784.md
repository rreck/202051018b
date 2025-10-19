```json
{
  "id": "cb48ff0e96777527",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288784,
  "host_pid": "9e6742732c60:1",
  "hash": "09f0fccab49533a4741155fd62c66f6079da5d7a18792119089ac6764bceb9c4",
  "cid": "QmV109f0fccab49533a4741155fd62c66f6079da5d7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288784,
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
      "evaluated_at": 1760288784
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
  "sig": "0238df485ebbb08596e76a243169ff7d478871fc64ab267aaa6ec7b5204fe0ab"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 122105158843417
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 816845640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285763, 'matching_hash': '108807581913276f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.06, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7854285}}}