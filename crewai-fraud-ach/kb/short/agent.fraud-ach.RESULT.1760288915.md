```json
{
  "id": "9d6b5ed7a9058799",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288915,
  "host_pid": "9e6742732c60:1",
  "hash": "c1d6ef54fc1dfc4c4ff362fe620f632173ae6625adf1b7b3cc1e5fa70062ef6c",
  "cid": "QmV1c1d6ef54fc1dfc4c4ff362fe620f632173ae6625",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288915,
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
      "evaluated_at": 1760288915
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "67fe69256b845fb7d0ba3619225040dea6910a4d01192dfe0406743c060eb040"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469028209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 26367012, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': 'a4269a968e85dafe'}}}aly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8542478}}}