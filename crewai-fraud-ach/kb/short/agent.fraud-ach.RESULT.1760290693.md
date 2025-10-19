```json
{
  "id": "0bf5b357c8606de4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290693,
  "host_pid": "9e6742732c60:1",
  "hash": "ab2f1f7cca497edf314e65661109c04b065875eabc0fce2c4d7a90cadc547178",
  "cid": "QmV1ab2f1f7cca497edf314e65661109c04b065875ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290693,
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
      "evaluated_at": 1760290693
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
  "sig": "26c53d31063be39f7c20f8ca020300216424ad1da6dea67bf11c699b364f85bf"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100277197484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 1561739916, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '4232e93b8d4c62d2'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.25, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9947388}}}