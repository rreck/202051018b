```json
{
  "id": "1f0edb8805f2d19b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286955,
  "host_pid": "9e6742732c60:1",
  "hash": "b028875f90231383a802ccb76e0530548f95b121f86aace6a8fdeed11b310aa1",
  "cid": "QmV1b028875f90231383a802ccb76e0530548f95b121",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286955,
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
      "evaluated_at": 1760286955
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "d25cdd8206801eeae3fc7160de6d118f1f0302864a2d57f3daf16239384d3d09"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201462613659
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 265672576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285764, 'matching_hash': '5c1e39699924121a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6178432}}}