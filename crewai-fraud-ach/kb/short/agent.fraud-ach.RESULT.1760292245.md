```json
{
  "id": "2f787c78b2d7c813",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292245,
  "host_pid": "9e6742732c60:1",
  "hash": "3f0faf5ad5e39d3a9b40ca6e70ed960d3906d4012f563dc06e9ba7f05067d5f8",
  "cid": "QmV13f0faf5ad5e39d3a9b40ca6e70ed960d3906d401",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292245,
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
      "evaluated_at": 1760292245
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
  "sig": "3f17f7462871beeb0f1ddb8d021be7bcc0569113e362fd1e2b46d2033b9e314b"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 031201462394531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 1473954510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '046e1c7f2d74b138'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.94, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7637070}}}