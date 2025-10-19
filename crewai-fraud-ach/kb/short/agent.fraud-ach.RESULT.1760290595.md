```json
{
  "id": "3ea2641a13e0deba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290595,
  "host_pid": "9e6742732c60:1",
  "hash": "67700771dfc53046c28121bc35edc19ffa0885694e522c94219ae800a0d5aab5",
  "cid": "QmV167700771dfc53046c28121bc35edc19ffa088569",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290595,
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
      "evaluated_at": 1760290595
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
  "sig": "6f77753d2a2faa52038fe1fa8d47ef873777e8acac213e7409e9609a490e64de"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 121000242463666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 1203553582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285764, 'matching_hash': '3cd63f27035973d0'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.04, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7815283}}}