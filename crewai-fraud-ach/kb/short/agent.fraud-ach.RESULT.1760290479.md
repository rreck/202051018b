```json
{
  "id": "e8786ef52c77c037",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290479,
  "host_pid": "9e6742732c60:1",
  "hash": "fddb26ab8e83ae567cdbf0f9ada31413cb689422b7013daf70efb27dc4b05682",
  "cid": "QmV1fddb26ab8e83ae567cdbf0f9ada31413cb689422",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290479,
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
      "evaluated_at": 1760290479
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
  "sig": "eb0b8727fe81f402182c7069d6b973b9b1d38d7a8e9e5875c52ce0d70b8168da"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 121000242247066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 1372100760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285765, 'matching_hash': '1251c161514af894'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.76, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9086760}}}