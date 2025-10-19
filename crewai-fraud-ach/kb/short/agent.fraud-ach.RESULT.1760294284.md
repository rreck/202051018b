```json
{
  "id": "731f997b9614d0c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294284,
  "host_pid": "9e6742732c60:1",
  "hash": "0551589e29fac2d93a8d73d6d2b02f080abf422d00748be9ecd0363f3d205c61",
  "cid": "QmV10551589e29fac2d93a8d73d6d2b02f080abf422d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294284,
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
      "evaluated_at": 1760294284
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
  "sig": "df6dff39d453301f32cdab19b52ab82f9e5b9c9f61abb1ad23cb389c9b05de65"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 031201462613659
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 1451931520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285764, 'matching_hash': '5c1e39699924121a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.11, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6178432}}}