```json
{
  "id": "01e8c878c90f7dbb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289054,
  "host_pid": "9e6742732c60:1",
  "hash": "c975cc4abcd87e723a4dc39ca5874f51683b5eefe0130b2b5a85f4311d76c439",
  "cid": "QmV1c975cc4abcd87e723a4dc39ca5874f51683b5eef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289054,
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
      "evaluated_at": 1760289054
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
  "sig": "439c35d2bf0f949ed67e8e4b06a573b5d7e9f770732be51b3d7d82ae7f56c302"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 063100275656907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 771956528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285764, 'matching_hash': '3d5aab5dd753a251'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6892469}}}