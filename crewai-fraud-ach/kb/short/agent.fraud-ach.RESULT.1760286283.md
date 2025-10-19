```json
{
  "id": "9d02e74a24060837",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286283,
  "host_pid": "9e6742732c60:1",
  "hash": "bc844df214b39142ddf154d48d5734bd9add7442328c623ee5479b4139c5c522",
  "cid": "QmV1bc844df214b39142ddf154d48d5734bd9add7442",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286283,
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
      "evaluated_at": 1760286283
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
  "sig": "a37f9a6aa0abbfacaf1827203f22d1c02d964136a0dffef703f2cc691ed03673"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 063100275758456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 188342980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285765, 'matching_hash': 'e3feb2a34db32d71'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.58, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9417149}}}