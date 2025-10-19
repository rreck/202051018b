```json
{
  "id": "7ab25a40b1185b52",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290655,
  "host_pid": "9e6742732c60:1",
  "hash": "425f194db1b5bf87725471ba27a2ba62088f08427622db62cdb50b064ddb8f96",
  "cid": "QmV1425f194db1b5bf87725471ba27a2ba62088f0842",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290655,
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
      "evaluated_at": 1760290655
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
  "sig": "e525f6d6b20ee8037ca54c63c728e3171056ba863b591acaf5042c30588307b1"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 031201465065641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 961190724, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': 'c71bd5f7fa32abe1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.1, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6161479}}}