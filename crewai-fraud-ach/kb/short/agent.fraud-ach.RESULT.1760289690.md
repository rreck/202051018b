```json
{
  "id": "04598b5c2f6134a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289690,
  "host_pid": "9e6742732c60:1",
  "hash": "60b7c5feb9f89b04186eaccfdaeb417e01740effdac7df57ad8518ec841e3b61",
  "cid": "QmV160b7c5feb9f89b04186eaccfdaeb417e01740eff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289690,
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
      "evaluated_at": 1760289690
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
  "sig": "61cf03b6555190d66a2df71f828163860166b70b0ca67894e4cd22d1df496a6d"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 044000033143138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 1157152230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285764, 'matching_hash': '6d0d609b65d243f3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 86, 'details': {'zscore': 4.65, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8901171}}}