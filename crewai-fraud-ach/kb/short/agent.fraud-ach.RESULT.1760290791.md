```json
{
  "id": "304c3d88601d58a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290791,
  "host_pid": "9e6742732c60:1",
  "hash": "d3848e5ae6b13e4c9dad30be25f1d01c83f682531a7ac39960f16d91fcaa9b5a",
  "cid": "QmV1d3848e5ae6b13e4c9dad30be25f1d01c83f68253",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290791,
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
      "evaluated_at": 1760290791
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
  "sig": "ae4facf272d3cd4221821ff9e43fe8d4f444fe7ed34d9e9c8f4292f4f7ba330e"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009597367941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 1479670854, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285764, 'matching_hash': '5430161f1ba10767'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.89, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9306106}}}