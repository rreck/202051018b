```json
{
  "id": "52fec80b6fa27280",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288216,
  "host_pid": "9e6742732c60:1",
  "hash": "8418d74b684b284fb9c7d09c805e4a94f86a633e87f90d5f77e817fe561a50b7",
  "cid": "QmV18418d74b684b284fb9c7d09c805e4a94f86a633e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288216,
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
      "evaluated_at": 1760288216
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
  "sig": "6c4687bc4113c4c8ca6514bff490f040f25dd61b5198041824f0e04362582b77"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 031201464331888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 544617962, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285764, 'matching_hash': '6a7d940bcd4512ca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6332767}}}