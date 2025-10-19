```json
{
  "id": "47756eb3a7e473a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286376,
  "host_pid": "9e6742732c60:1",
  "hash": "e5d0b9dcbabde920d894c254c5c7d5847b54c9cfe0dfe0ef40296c41adf5dfec",
  "cid": "QmV1e5d0b9dcbabde920d894c254c5c7d5847b54c9cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286376,
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
      "evaluated_at": 1760286376
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
  "sig": "2dde48930c94bb29490e1c363f9df67a0adab6f03c555c0cf7c8fe6d00c9ded3"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 063100275758456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 216594427, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285765, 'matching_hash': 'e3feb2a34db32d71'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.58, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9417149}}}