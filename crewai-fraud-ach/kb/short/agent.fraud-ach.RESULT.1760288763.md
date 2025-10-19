```json
{
  "id": "66ab0d22b9006419",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288763,
  "host_pid": "9e6742732c60:1",
  "hash": "690138ba5c87fdff83850f0911e99ae779079cc01598ca702921b7ea63871b88",
  "cid": "QmV1690138ba5c87fdff83850f0911e99ae779079cc0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288763,
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
      "evaluated_at": 1760288763
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
  "sig": "bc15f8c9841cbfbb419038ca624e4df4115cb9b82e942d15dea2456460857767"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 044000033143138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 916820613, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285764, 'matching_hash': '6d0d609b65d243f3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 86, 'details': {'zscore': 4.65, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8901171}}}