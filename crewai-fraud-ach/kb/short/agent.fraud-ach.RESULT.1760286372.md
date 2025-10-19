```json
{
  "id": "eecf0f5110efe1d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286372,
  "host_pid": "9e6742732c60:1",
  "hash": "16d14a70711f594b0c8f9878e3302836b4c9d529fa81b174c3b4b4cdcd29f320",
  "cid": "QmV116d14a70711f594b0c8f9878e3302836b4c9d529",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286372,
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
      "evaluated_at": 1760286372
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
  "sig": "f2081c9bbddcc45c683adf0e68c5f8abae7d06aee88d5c5e64f6c7585f697ee3"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 121000242202372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 214435601, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '7eed822364ae6d91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.54, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9323287}}}