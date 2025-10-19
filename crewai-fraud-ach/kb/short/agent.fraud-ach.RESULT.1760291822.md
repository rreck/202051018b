```json
{
  "id": "71ce96fe9ce2e6ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291822,
  "host_pid": "9e6742732c60:1",
  "hash": "201cb1a63c2e068877404871fee38d4e2f00d218f91f791b24fd7be57cd8790c",
  "cid": "QmV1201cb1a63c2e068877404871fee38d4e2f00d218",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291822,
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
      "evaluated_at": 1760291822
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
  "sig": "7ab2134e05f2b350eb252f3a74d5987b2e25455ecac38e4314bf5e031311e39b"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 044000036587475
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 1415863072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '7583721e7662209c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.97, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7694908}}}