```json
{
  "id": "ef44b08b7f9e40a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291328,
  "host_pid": "9e6742732c60:1",
  "hash": "1f49b3e996ca99f3ffb49e3bed4cbbd967edc861c7684dc4556ad800b236e1d4",
  "cid": "QmV11f49b3e996ca99f3ffb49e3bed4cbbd967edc861",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291328,
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
      "evaluated_at": 1760291328
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
  "sig": "4cd377acf25f86fc0bb4f883bca05d91ea04096fa026cacc4920fb50ac6789e2"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 063100272253110
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 1185336108, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285764, 'matching_hash': 'c9de6cf87e9b501f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6891489}}}