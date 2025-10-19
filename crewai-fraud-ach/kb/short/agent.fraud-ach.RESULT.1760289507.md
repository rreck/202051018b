```json
{
  "id": "fa068d93d166d269",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289507,
  "host_pid": "9e6742732c60:1",
  "hash": "ed086609016fe368aced3a0311e68ae3783e02146ff3b43d7df2cdb187b1d10e",
  "cid": "QmV1ed086609016fe368aced3a0311e68ae3783e0214",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289507,
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
      "evaluated_at": 1760289507
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
  "sig": "ab0ac996ae4ac058ba69a7b455741e0eeeff82725a1aa477e3d6608a2bd5bcd0"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 044000031749582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 784506125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285765, 'matching_hash': '509963b8d6b047dd'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.16, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6276049}}}