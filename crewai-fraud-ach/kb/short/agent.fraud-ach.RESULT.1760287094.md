```json
{
  "id": "091833f65406a8b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287094,
  "host_pid": "9e6742732c60:1",
  "hash": "6aaf80f1a89ad969d4364fb189f14c54ef25a1cadd0f1e5bc5c571fe2be82c2b",
  "cid": "QmV16aaf80f1a89ad969d4364fb189f14c54ef25a1ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287094,
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
      "evaluated_at": 1760287094
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
  "sig": "7a28cdeb8ddc4b6a89d897ecb0d45705d6e04074acae6ceaa08894c1ac9d8b8d"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 122105155084324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 330018048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285763, 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6875376}}} {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9410889}}}