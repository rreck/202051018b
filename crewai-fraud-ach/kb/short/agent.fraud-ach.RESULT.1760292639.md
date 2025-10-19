```json
{
  "id": "fe2f622cb1a5dc9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292639,
  "host_pid": "9e6742732c60:1",
  "hash": "6b3d6e76d6ef29f27ac449c8278c5df6e848eccede2f26596460f2605b3439ce",
  "cid": "QmV16b3d6e76d6ef29f27ac449c8278c5df6e848ecce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292639,
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
      "evaluated_at": 1760292640
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
  "sig": "d76b7b9773cd5f5c3053d164c8b754b8eea45d146b45dbc964d1914143094afa"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 111000023893131
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 1983160452, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': '5255bec7f5e0b39d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.18, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9817626}}}