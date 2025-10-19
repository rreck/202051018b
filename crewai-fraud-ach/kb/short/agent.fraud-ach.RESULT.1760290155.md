```json
{
  "id": "849055d80264f3af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290155,
  "host_pid": "9e6742732c60:1",
  "hash": "b99b0077eb3710179e585443559856ca7d6a8c7653e71ee6ba8c6ee8fe100a36",
  "cid": "QmV1b99b0077eb3710179e585443559856ca7d6a8c76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290155,
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
      "evaluated_at": 1760290155
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
  "sig": "12bf9cdb924c132f159bf7bc279b5fd4bc9be3729d6ce03060d3af9625e03c29"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 122105155084324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 983178768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.5, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6875376}}}