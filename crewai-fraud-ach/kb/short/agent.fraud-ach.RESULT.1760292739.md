```json
{
  "id": "b7c959c680664095",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292739,
  "host_pid": "9e6742732c60:1",
  "hash": "173737c82e2de4dda45e09a114db691236136171a035f9bda79dbc1566850746",
  "cid": "QmV1173737c82e2de4dda45e09a114db691236136171",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292739,
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
      "evaluated_at": 1760292739
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
  "sig": "cf5e07b844302c0287f4596ce6b4e1b6c9b10357120f826f10f96f6da16d2c4b"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009598883007
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 1947448668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285764, 'matching_hash': '3affdb087741de2d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9546317}}}