```json
{
  "id": "3f964c2edd3c307e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287416,
  "host_pid": "9e6742732c60:1",
  "hash": "b239adac6954dab1b5c4290948fbd7e2289abd506b1c686e2cb240801ad9199c",
  "cid": "QmV1b239adac6954dab1b5c4290948fbd7e2289abd50",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287416,
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
      "evaluated_at": 1760287416
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
  "sig": "2b0bd48e7b6248792199f501e945a782419adabd2e9c60c634ab0681c93ef389"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 121000240089409
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 362202770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285765, 'matching_hash': 'a79d0bf31de09717'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6139030}}}