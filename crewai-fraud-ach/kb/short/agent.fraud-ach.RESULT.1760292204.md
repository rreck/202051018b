```json
{
  "id": "3db145fdd6071432",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292204,
  "host_pid": "9e6742732c60:1",
  "hash": "91c038d9a726d1c5ba2f72235426c1a7b1dcd0f2e48e66e9c2ff1aeb51a90613",
  "cid": "QmV191c038d9a726d1c5ba2f72235426c1a7b1dcd0f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292204,
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
      "evaluated_at": 1760292204
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
  "sig": "6156a98cd4b25a93245ac5bf81960d9d864a6d2e292e0f7f9a189f3fa32bb33a"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 031201467009203
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 1523284224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285765, 'matching_hash': 'e7911512dd8ff7c4'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.1, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7933772}}}