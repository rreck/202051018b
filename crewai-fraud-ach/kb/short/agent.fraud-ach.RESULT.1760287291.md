```json
{
  "id": "79aa30f608c94cdc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287291,
  "host_pid": "9e6742732c60:1",
  "hash": "fff355745c53ce312a050aff10af619b93bf8e71bf14c5931829155e7cc23ed4",
  "cid": "QmV1fff355745c53ce312a050aff10af619b93bf8e71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287291,
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
      "evaluated_at": 1760287291
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "240711b50fa1448a1d77f11d370d88ee6fa5638494ecfd8f2f18fb7a5fcc7c52"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000029709484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 22513040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285763, 'matching_hash': 'f2d4d1f000649e92'}}}aly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.76, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9817626}}}