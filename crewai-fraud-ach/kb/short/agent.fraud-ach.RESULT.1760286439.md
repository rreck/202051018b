```json
{
  "id": "7b3c0512ad291dd9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286439,
  "host_pid": "9e6742732c60:1",
  "hash": "ab2f35805798a3f117bd8c1a6944490b06f1b83eeca034ee5a71b0b5b20e9dec",
  "cid": "QmV1ab2f35805798a3f117bd8c1a6944490b06f1b83e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286439,
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
      "evaluated_at": 1760286439
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
  "sig": "755b6f9d60a7cbdae03b6d88dda128f3a9caf0da6d0ba0f0d1b6e40efb9dd236"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 021000024248654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 193848725, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285765, 'matching_hash': '6adb7b11c0829b91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7753949}}}