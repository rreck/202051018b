```json
{
  "id": "21a216c287271bf1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294613,
  "host_pid": "9e6742732c60:1",
  "hash": "7fda8792695f599866a6f1fd392f9fd31b692227b3923b73bb28a1dd97b1fe58",
  "cid": "QmV17fda8792695f599866a6f1fd392f9fd31b692227",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294613,
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
      "evaluated_at": 1760294613
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
  "sig": "70b8a4796ea7f8a2d5b9312133e11a230e68a79906e3f19a715982484992b0b3"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 044000031749582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 1512527809, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285765, 'matching_hash': '509963b8d6b047dd'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.16, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6276049}}}