```json
{
  "id": "377b47b08de51e45",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292615,
  "host_pid": "9e6742732c60:1",
  "hash": "658b601efc987b870df395a43d5a66ba027cb72198ea105fdfa5eb234ab2e5b0",
  "cid": "QmV1658b601efc987b870df395a43d5a66ba027cb721",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292615,
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
      "evaluated_at": 1760292615
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
  "sig": "acc85e4eb687d28db51e8a9d4f78ae26ac8c4f2c0d049c2c487a4bc438b9eade"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 063100272253110
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 1385189289, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285764, 'matching_hash': 'c9de6cf87e9b501f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6891489}}}