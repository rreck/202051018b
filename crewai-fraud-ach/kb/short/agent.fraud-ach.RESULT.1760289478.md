```json
{
  "id": "9741b22570e89e1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289478,
  "host_pid": "9e6742732c60:1",
  "hash": "77cd41cec8d76ece3b9c3fbb2d611a1c45be62be2959857b4c587182715a314f",
  "cid": "QmV177cd41cec8d76ece3b9c3fbb2d611a1c45be62be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289478,
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
      "evaluated_at": 1760289478
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
  "sig": "18fb342967f750a5dd5abcd38e6109d07632f716eb60ca151a492875838d180d"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 031201464331888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 785263108, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285764, 'matching_hash': '6a7d940bcd4512ca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.19, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6332767}}}