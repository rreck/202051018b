```json
{
  "id": "6d4b7b3b4c6018b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290113,
  "host_pid": "9e6742732c60:1",
  "hash": "8475cc4a02b058dadd4c672a4dc66b0b5fae5f0efc9e55c0ab5a60d8d7f19ce9",
  "cid": "QmV18475cc4a02b058dadd4c672a4dc66b0b5fae5f0e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290113,
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
      "evaluated_at": 1760290113
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
  "sig": "90fa0617156e1a170ed81bd8f47a3602bb7e1c51bcc7bb3b7267fe26f6db8e2b"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 111000024041930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 1045947860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': 'd0d1b4b42d54423e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.78, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7365830}}}