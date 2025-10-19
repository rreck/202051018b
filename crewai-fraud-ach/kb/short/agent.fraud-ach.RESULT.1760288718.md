```json
{
  "id": "f615147d1a9cf73d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288718,
  "host_pid": "9e6742732c60:1",
  "hash": "ac830a8bd2a9caf250ff7561eba7bb9591149665a76db4b697b47dc33f097648",
  "cid": "QmV1ac830a8bd2a9caf250ff7561eba7bb9591149665",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288718,
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
      "evaluated_at": 1760288718
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
  "sig": "a959b91fc55412625e12277bff644b8bbf312f145ae9daacfe5bb0dee9ca010b"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100277197484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 1014633576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': '4232e93b8d4c62d2'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.25, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9947388}}}