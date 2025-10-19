```json
{
  "id": "a7fe74e96ed177f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290875,
  "host_pid": "9e6742732c60:1",
  "hash": "e415340c6c6d1db1f0340eb680a94e938bbe5f266763f204d5ddba437f98d20a",
  "cid": "QmV1e415340c6c6d1db1f0340eb680a94e938bbe5f26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290875,
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
      "evaluated_at": 1760290875
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
  "sig": "75bd55413680b7295446b041f2ee647bb8d8a28dde7a2de3f9402b80f0153e4b"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 031201467009203
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 1277337292, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285765, 'matching_hash': 'e7911512dd8ff7c4'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.1, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7933772}}}