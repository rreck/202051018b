```json
{
  "id": "175c1b6ff0d5a1cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292930,
  "host_pid": "9e6742732c60:1",
  "hash": "085dfc39dc0d8bd29bddf4aa1d961f2dc8504bf6ac8e1a9257b9e7ff62254455",
  "cid": "QmV1085dfc39dc0d8bd29bddf4aa1d961f2dc8504bf6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292930,
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
      "evaluated_at": 1760292930
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
  "sig": "483eb4163864cca93c7d39f70672f74b8cf7dd4fbe1d8df973c9bb0bb715ff47"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 121000246089162
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 1860106976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285764, 'matching_hash': '13ee20e814facee3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 86, 'details': {'zscore': 4.68, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8942822}}}