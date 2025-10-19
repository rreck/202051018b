```json
{
  "id": "58d2b3641b8dd783",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292227,
  "host_pid": "9e6742732c60:1",
  "hash": "1b9db71159ecf52863761ed3ab84d4c7e6451a65f10495cc1aa041b14269dbbd",
  "cid": "QmV11b9db71159ecf52863761ed3ab84d4c7e6451a65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292227,
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
      "evaluated_at": 1760292227
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
  "sig": "8e27d31f063a5174293a9e6670ec6ecc137f7e81e442c5f582b16e7684fc2700"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 122105155084324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 1326947568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.5, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6875376}}}