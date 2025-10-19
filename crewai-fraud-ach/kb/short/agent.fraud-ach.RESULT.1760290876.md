```json
{
  "id": "fd2b2edc37da85e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290876,
  "host_pid": "9e6742732c60:1",
  "hash": "f6eb274bb091ba82e325c438e8954d3ba83087bf362aac21163cf00b3f4fe1a9",
  "cid": "QmV1f6eb274bb091ba82e325c438e8954d3ba83087bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290876,
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
      "evaluated_at": 1760290876
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
  "sig": "62d89ea16aa6ada7a4c7d59c8e259ad11f58ebd9fc6d01db6ba01d91e6572c90"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 044000032002639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 1279760825, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285765, 'matching_hash': '27a8182d1a86d123'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7948825}}}