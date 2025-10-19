```json
{
  "id": "bf75b866d6b629ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289930,
  "host_pid": "9e6742732c60:1",
  "hash": "4be461f71f64f710b33229bfbf48e8690906a2cf39cc3f919c9b2f8034a8ea15",
  "cid": "QmV14be461f71f64f710b33229bfbf48e8690906a2cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289930,
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
      "evaluated_at": 1760289931
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
  "sig": "a52c992c9d9fa170b7efae1c37f7a2a39abd005f835abff2511e3fa96f654ee0"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 122105158843417
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 1076037045, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '108807581913276f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.06, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7854285}}}