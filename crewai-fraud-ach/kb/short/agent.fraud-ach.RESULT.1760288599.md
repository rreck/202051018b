```json
{
  "id": "fac30398e3d9d0bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288599,
  "host_pid": "9e6742732c60:1",
  "hash": "b6ab049e4f1618b8d3d1a6b22ee3fbd02584df0ce0ffa10322396b8a9db5beab",
  "cid": "QmV1b6ab049e4f1618b8d3d1a6b22ee3fbd02584df0c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288599,
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
      "evaluated_at": 1760288599
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
  "sig": "506bd6245f9dbe5850ae6d4c7a6c966be309f387a7196374322fd9eb7a4b2c11"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 121000242202372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 913682126, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': '7eed822364ae6d91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.9, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9323287}}}