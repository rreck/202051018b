```json
{
  "id": "689264d78e36112f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288468,
  "host_pid": "9e6742732c60:1",
  "hash": "a821abea2d824b85edaa354cbbae6e8c3ae5715e5276b594c2d6643d8385520a",
  "cid": "QmV1a821abea2d824b85edaa354cbbae6e8c3ae5715e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288468,
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
      "evaluated_at": 1760288468
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
  "sig": "d10b78ba460fe0a525a43990103692d4aa2c2714ccee682beff9a0ce506bc58b"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 031201462394531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 717884580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '046e1c7f2d74b138'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7637070}}}