```json
{
  "id": "246cc59dcec19c97",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286705,
  "host_pid": "9e6742732c60:1",
  "hash": "2e7b2b6f81dcbf80e83bca512e32016a9a14608e547a34b1b0e47c0d4ed84846",
  "cid": "QmV12e7b2b6f81dcbf80e83bca512e32016a9a14608e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286705,
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
      "evaluated_at": 1760286705
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
  "sig": "045ce550f219041d91e31e1908518acadc99bf9376babcc75e8ad5dd821a0bb2"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 063100275758456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 320183066, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285765, 'matching_hash': 'e3feb2a34db32d71'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.58, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9417149}}}