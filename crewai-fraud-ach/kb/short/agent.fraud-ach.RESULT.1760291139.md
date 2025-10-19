```json
{
  "id": "cfc2cb78a00faec7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291139,
  "host_pid": "9e6742732c60:1",
  "hash": "59aad39fcefac5e6efda0d2fb636fa2c0f0fada919c2c0ae84af1cfbb20405b7",
  "cid": "QmV159aad39fcefac5e6efda0d2fb636fa2c0f0fada9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291139,
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
      "evaluated_at": 1760291139
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
  "sig": "455d50ebefe1085226db81e52a8b5d639ddd594a5ff3d8beb9f90cc12c430f7f"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 122105154811722
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 1258938240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': 'f2f6645498600029'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 78, 'details': {'zscore': 3.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7493680}}}