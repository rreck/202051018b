```json
{
  "id": "fbbd2268d594d74a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291391,
  "host_pid": "9e6742732c60:1",
  "hash": "9ae8966910770ca05077c3cfbb0fdff99ef4e55d2f5404f56794878816a0046b",
  "cid": "QmV19ae8966910770ca05077c3cfbb0fdff99ef4e55d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291391,
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
      "evaluated_at": 1760291391
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
  "sig": "60e56d13939430eb5cd8588482d0e7b94d9708e2414ca1051caf2bc37de9380d"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 021000024856185
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 1245305646, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': '03b6a41c39a9a2ab'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.66, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7156929}}}