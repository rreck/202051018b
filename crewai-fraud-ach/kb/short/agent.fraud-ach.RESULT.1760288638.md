```json
{
  "id": "384437ec56f5bf16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288638,
  "host_pid": "9e6742732c60:1",
  "hash": "ca4cce29b0faf762abcdb3d448c9e1109401879afec15dbed19d58617abc0197",
  "cid": "QmV1ca4cce29b0faf762abcdb3d448c9e1109401879a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288638,
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
      "evaluated_at": 1760288638
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
  "sig": "aeda0f268566d9d095f6e41a92ffb627b82cd9f3eb1b74203de084188638c9a7"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000026914318
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 968585310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285765, 'matching_hash': '634436741ef501a5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9783690}}}