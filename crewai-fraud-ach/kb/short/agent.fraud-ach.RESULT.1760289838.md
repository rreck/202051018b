```json
{
  "id": "6ae59bfe30a217ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289838,
  "host_pid": "9e6742732c60:1",
  "hash": "c348255cd479b934ddf3c0f4f3b8ac2aade3fa6a611cd5bf7aecda7af7004850",
  "cid": "QmV1c348255cd479b934ddf3c0f4f3b8ac2aade3fa6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289838,
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
      "evaluated_at": 1760289838
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
  "sig": "c079893b1852f6de8f5bc37700d57704dd47eea2af7a570de92d6a8c270706a0"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 121000241325245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 1093393770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': '97920a0a35eda98b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 82, 'details': {'zscore': 4.23, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8159655}}}