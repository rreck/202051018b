```json
{
  "id": "3dfdfd43c35fe2a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289465,
  "host_pid": "9e6742732c60:1",
  "hash": "4ce1f37e70183fcc0c71d4501e8493d271e62b87cff73177aaf04705813b10ae",
  "cid": "QmV14ce1f37e70183fcc0c71d4501e8493d271e62b87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289465,
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
      "evaluated_at": 1760289465
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
  "sig": "704f8bedd2cbb19ec29416207c27b4c01578e9a0dc15cc5fb5ccb49dd4d9c610"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009598883007
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 1183743308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285764, 'matching_hash': '3affdb087741de2d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9546317}}}