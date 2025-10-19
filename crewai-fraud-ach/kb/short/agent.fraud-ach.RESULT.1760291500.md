```json
{
  "id": "4f913364da08a0b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291500,
  "host_pid": "9e6742732c60:1",
  "hash": "50f9c280965d007048a70b202d1278c5dfaf046328cffd51503c756b6fee6c68",
  "cid": "QmV150f9c280965d007048a70b202d1278c5dfaf0463",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291500,
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
      "evaluated_at": 1760291500
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
  "sig": "c8b38eec419e776f57301d0bb43eac424d258e804739796b81f3f38bdf9dc879"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 121000242247066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 1599269760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': '1251c161514af894'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.76, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9086760}}}