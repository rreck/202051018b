```json
{
  "id": "86f0cc8d9f99fbde",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286559,
  "host_pid": "9e6742732c60:1",
  "hash": "c0af4480e60cec02bc1915cb762105ad174e9d7efdc7620a98dd89178ffff528",
  "cid": "QmV1c0af4480e60cec02bc1915cb762105ad174e9d7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286559,
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
      "evaluated_at": 1760286559
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
  "sig": "1194b6a553d21d50684128eeed1d20864799291cc8b572467b2e512db2ed9b55"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 121000242463666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 226643207, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285764, 'matching_hash': '3cd63f27035973d0'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7815283}}}