```json
{
  "id": "b586f0bb64c8e60c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288852,
  "host_pid": "9e6742732c60:1",
  "hash": "a4ed4a18c225bd4cd07d3bba02a53e5b1c2d598f7133750562f85496b52e5ef3",
  "cid": "QmV1a4ed4a18c225bd4cd07d3bba02a53e5b1c2d598f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288852,
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
      "evaluated_at": 1760288852
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
  "sig": "f331e302ef7dbedc5b7a907d187bf36b434e5ac7a1e40e58ac7a6688772e78a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155818462
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 34747860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '4e45a5675434ecee'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}