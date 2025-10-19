```json
{
  "id": "38ac1f198c998c69",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293028,
  "host_pid": "9e6742732c60:1",
  "hash": "0eceb32f564ca112f59fb26169177b1b33cba0bec7f238e431867976fb1239ca",
  "cid": "QmV10eceb32f564ca112f59fb26169177b1b33cba0be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293028,
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
      "evaluated_at": 1760293028
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
  "sig": "d5c3f6ef77c4385027b17ad9f3121a28171dbc1e67582da36fffb7453c372047"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 021000029420003
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 1386539700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285764, 'matching_hash': '37b4044b8dabc650'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.35, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6602570}}}