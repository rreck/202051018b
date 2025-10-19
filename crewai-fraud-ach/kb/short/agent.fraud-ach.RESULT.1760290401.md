```json
{
  "id": "aa7e14f7af10636e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290401,
  "host_pid": "9e6742732c60:1",
  "hash": "72660c52997dfa5c027c35810f39a78cf4f62fb1c61c72c03d40e4bf35040db2",
  "cid": "QmV172660c52997dfa5c027c35810f39a78cf4f62fb1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290401,
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
      "evaluated_at": 1760290401
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
  "sig": "45cc3ee6523202373901e372b0d1f795c15a22e274c32bed369fa37a06d3762d"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 031201464331888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 943582283, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285764, 'matching_hash': '6a7d940bcd4512ca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.19, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6332767}}}