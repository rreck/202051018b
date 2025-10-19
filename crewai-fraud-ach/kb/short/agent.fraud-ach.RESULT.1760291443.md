```json
{
  "id": "69c239d4f7555d02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291443,
  "host_pid": "9e6742732c60:1",
  "hash": "90440394c81e4b162d3d0e6da82d2cefdf5b823c59b3b82056c53d95bd6b8988",
  "cid": "QmV190440394c81e4b162d3d0e6da82d2cefdf5b823c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291443,
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
      "evaluated_at": 1760291443
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
  "sig": "b2a6571f0f78f75452e3ee76260bafaf0f9257020742934c336088d643c0b86e"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 031201462613659
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 1081225600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285764, 'matching_hash': '5c1e39699924121a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6178432}}}