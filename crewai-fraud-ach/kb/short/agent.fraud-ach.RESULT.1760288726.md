```json
{
  "id": "1a05cdc64afc1029",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288726,
  "host_pid": "9e6742732c60:1",
  "hash": "5a75e9f4af56d25d675d883f26b6046c21fbfbbc2d288c3e37b52345f3b4f555",
  "cid": "QmV15a75e9f4af56d25d675d883f26b6046c21fbfbbc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288726,
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
      "evaluated_at": 1760288726
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
  "sig": "287e212f5ea99604516c0d05c2b0cfdc56a90bdccdd080da4f5affa0d02ebd91"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 044000039260642
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 996032464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760284979, 'matching_hash': 'a7542f9d69c5b02c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5595688}}}bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7743228}}}