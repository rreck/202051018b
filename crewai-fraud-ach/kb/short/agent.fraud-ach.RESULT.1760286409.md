```json
{
  "id": "48ecb56f3345a759",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286409,
  "host_pid": "9e6742732c60:1",
  "hash": "8599599d5863c1559b8d00028b247a7c92430a05518b1a3a1e0efe81b1ce3457",
  "cid": "QmV18599599d5863c1559b8d00028b247a7c92430a05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286409,
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
      "evaluated_at": 1760286409
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
  "sig": "7b17ffc0d828f9e2eefcbdd685a06ec1deaaf9c0332242d387f7790046aed407"
}
```

Fraud detected: amount_anomaly (score: 75)
Transaction: 121000241325245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 195831720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285765, 'matching_hash': '97920a0a35eda98b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.02, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8159655}}}