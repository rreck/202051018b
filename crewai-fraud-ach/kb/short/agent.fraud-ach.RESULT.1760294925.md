```json
{
  "id": "f720b2af53f1f95f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294925,
  "host_pid": "9e6742732c60:1",
  "hash": "ae04cc03b18ddb3251f1f954539f8254251da560a159b35bb691649ed29797eb",
  "cid": "QmV1ae04cc03b18ddb3251f1f954539f8254251da560",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294925,
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
      "evaluated_at": 1760294925
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
  "sig": "1bfe0795d157fd9cc8afb8a399a51254b8bbb6c8cbab70ae734ddb281fb2b22d"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 026009593536261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 1701487658, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285764, 'matching_hash': 'ca8349fc21f82b4d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6888614}}}