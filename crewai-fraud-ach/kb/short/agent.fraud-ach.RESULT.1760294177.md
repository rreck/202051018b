```json
{
  "id": "b56a0ebf5fc30ce3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294177,
  "host_pid": "9e6742732c60:1",
  "hash": "06a93d188568f4aabd0f4b5ccb7b732faceb2a969246140951e7080fa431eb46",
  "cid": "QmV106a93d188568f4aabd0f4b5ccb7b732faceb2a96",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294177,
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
      "evaluated_at": 1760294177
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
  "sig": "d5bc0eed7d303d621370b01336e3cbdd53bee0bc9d6f58b9b59f94027ece7077"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 063100275656907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 1605945277, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': '3d5aab5dd753a251'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6892469}}}