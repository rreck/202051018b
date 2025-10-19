```json
{
  "id": "364ebf8e5daa480d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291201,
  "host_pid": "9e6742732c60:1",
  "hash": "a267de792c6bc97bb49b1dba1f11b233c7c9fc1bb3223d7cb966b7dde5cbeba9",
  "cid": "QmV1a267de792c6bc97bb49b1dba1f11b233c7c9fc1b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291201,
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
      "evaluated_at": 1760291201
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
  "sig": "5184faa411c248903b32bd5a031ae4c16e1f921be06c9677ac760df36d878462"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 122105153391998
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 1312228554, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285764, 'matching_hash': '05c5de8ca533802c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.01, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7764666}}}