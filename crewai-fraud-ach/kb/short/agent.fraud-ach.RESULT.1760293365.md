```json
{
  "id": "66450c4951b6be09",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293365,
  "host_pid": "9e6742732c60:1",
  "hash": "68060953d287c76815111873b1a952a78a42773212926602709e81584a80a1f4",
  "cid": "QmV168060953d287c76815111873b1a952a78a427732",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293365,
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
      "evaluated_at": 1760293365
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
  "sig": "5667df051f04a00521f86f62822b5f2e73f0a632966272178002c8c43b1e13a1"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 044000032483239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 2006236827, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': '7bd2e976d6ef9e3c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9245331}}}