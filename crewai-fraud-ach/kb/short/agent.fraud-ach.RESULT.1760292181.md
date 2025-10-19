```json
{
  "id": "7f76b9e99ac25718",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292181,
  "host_pid": "9e6742732c60:1",
  "hash": "6df15111394d72660ad65c4c17ce8e41e2a3a68ff28dc1513a52c1341415f4c7",
  "cid": "QmV16df15111394d72660ad65c4c17ce8e41e2a3a68f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292181,
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
      "evaluated_at": 1760292181
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
  "sig": "4dcbf229111ca58d4d276ccc034d67f7c0342cdb3dc284fede3bd190479a06b9"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 122105155084324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 1320072192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.5, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6875376}}}