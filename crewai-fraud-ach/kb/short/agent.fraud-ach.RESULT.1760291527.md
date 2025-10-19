```json
{
  "id": "ed1b408f280c661b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291527,
  "host_pid": "9e6742732c60:1",
  "hash": "9a7bb1e7251a4615a35ef41f89724b15fdceb933e9e639446a2c8ce993f2096f",
  "cid": "QmV19a7bb1e7251a4615a35ef41f89724b15fdceb933",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291527,
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
      "evaluated_at": 1760291527
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
  "sig": "aeb5865c48c93120f59ac841d2452057652bdc2358c9a0e8954772fa7c843099"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100270473682
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 1689926085, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': 'dcfb2900505c6ddc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9547605}}}