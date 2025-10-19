```json
{
  "id": "d8178af74154300d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286309,
  "host_pid": "9e6742732c60:1",
  "hash": "9ce058189c2cc289766de7d4b1cbb405c96e167396fa41f2a0c2aae36754e716",
  "cid": "QmV19ce058189c2cc289766de7d4b1cbb405c96e1673",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286309,
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
      "evaluated_at": 1760286309
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
  "sig": "addf5a856ff1af9c3079862cfaeafabedccfa064bdb7c1c3ec059c62b8c407fa"
}
```

Fraud detected: amount_anomaly (score: 75)
Transaction: 122105150198952
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 175022946, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285763, 'matching_hash': '35a36fb353493cca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.1, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8334426}}}