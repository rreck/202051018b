```json
{
  "id": "a0bb298c78f76839",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289168,
  "host_pid": "9e6742732c60:1",
  "hash": "c402a4f5eb3eb07ccecdb7481dffc8342442e01a95f56c2bab1121b5939c84ff",
  "cid": "QmV1c402a4f5eb3eb07ccecdb7481dffc8342442e01a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289168,
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
      "evaluated_at": 1760289168
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
  "sig": "be6c4f6d7c9fd4554aa9aaf04c5291ecb698ec00c37b960dd39cd3611dc7bc08"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 063100278543685
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 815276170, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285765, 'matching_hash': 'e9470cd0cc07fb40'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.62, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7089358}}}