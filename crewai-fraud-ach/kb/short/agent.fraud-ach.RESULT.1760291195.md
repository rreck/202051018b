```json
{
  "id": "2bddbf3062da8416",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291195,
  "host_pid": "9e6742732c60:1",
  "hash": "a6b41c8cf3ffff2c0da2bd01f28ea8d3429212f1aa74df46231e2644f79bc2df",
  "cid": "QmV1a6b41c8cf3ffff2c0da2bd01f28ea8d3429212f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291195,
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
      "evaluated_at": 1760291195
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
  "sig": "79d64e3ced7467d82b6b28ce88324624a8410280f9ca8fa7cb7c9a94c62a85ec"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 044000031749582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 1060652281, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285765, 'matching_hash': '509963b8d6b047dd'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.16, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6276049}}}