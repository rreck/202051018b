```json
{
  "id": "ddd5ed709b49dede",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292876,
  "host_pid": "9e6742732c60:1",
  "hash": "abb121ea18d7a3c9f904e659002348f2d372c6e70793badd095aa83e11cbfe42",
  "cid": "QmV1abb121ea18d7a3c9f904e659002348f2d372c6e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292876,
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
      "evaluated_at": 1760292876
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
  "sig": "84431f5bb43f2ca9a932dda7648fe9e915358621b5cf75fb42a837c92467469e"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 044000036587475
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 1592845956, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '7583721e7662209c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.97, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7694908}}}