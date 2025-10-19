```json
{
  "id": "ec88d3a0705dfa1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291185,
  "host_pid": "9e6742732c60:1",
  "hash": "25a249d493117c05562d188ebf8ae9a80df81119fcbffbeb04d5d23d2533dd3f",
  "cid": "QmV125a249d493117c05562d188ebf8ae9a80df81119",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291185,
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
      "evaluated_at": 1760291185
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
  "sig": "3753bc87c6aeb8caa12772468499349500a646fbbe9a6d7fecbcc1b1f3ccf33d"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009598883007
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 1613327573, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285764, 'matching_hash': '3affdb087741de2d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9546317}}}