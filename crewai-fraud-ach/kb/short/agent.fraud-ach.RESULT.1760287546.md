```json
{
  "id": "6c3f7edf608d75f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287546,
  "host_pid": "9e6742732c60:1",
  "hash": "084e2f15f4522fb71d47c9d45c63fa44ad58950476825c8a1dfa58ec06df0432",
  "cid": "QmV1084e2f15f4522fb71d47c9d45c63fa44ad589504",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287546,
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
      "evaluated_at": 1760287546
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "7f89d76ad18bbfaa38f46e78be635734b69bb6d1d271231092c65c6253c3b7e3"
}
```

Fraud detected: amount_anomaly (score: 74)
Transaction: 063100277645862
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 416732480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285764, 'matching_hash': 'c7c729dc286039c9'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6511445}}}