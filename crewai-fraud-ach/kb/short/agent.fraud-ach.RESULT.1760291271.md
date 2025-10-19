```json
{
  "id": "b93f2e5d96162971",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291271,
  "host_pid": "9e6742732c60:1",
  "hash": "e296108822a7978b3f90cbd50912192dc1f465786470b6fcc1825e898e911daf",
  "cid": "QmV1e296108822a7978b3f90cbd50912192dc1f46578",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291271,
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
      "evaluated_at": 1760291271
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
  "sig": "ac27f2080b542a61f6196d7bfa869bf7519ab23ff5bd177cfb34039ac080a029"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 021000025025802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 1371133575, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285764, 'matching_hash': 'd7be7bb127c676c6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018325}}}