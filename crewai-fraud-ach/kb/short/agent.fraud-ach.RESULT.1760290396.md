```json
{
  "id": "b57cbcdec61f50a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290396,
  "host_pid": "9e6742732c60:1",
  "hash": "25a80d8e74f5e6f3c446ef173226b509d8ce2537bf57d231cc5a8c5175e099d6",
  "cid": "QmV125a80d8e74f5e6f3c446ef173226b509d8ce2537",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290396,
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
      "evaluated_at": 1760290396
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
  "sig": "348a58030a146cfd93c6e27bb5fdbee01824e5f3eea712cee0af42fa22b3425b"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 111000024639540
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 1143134258, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285765, 'matching_hash': '9eefc6a12f8b62a3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.96, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7672042}}}