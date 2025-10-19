```json
{
  "id": "1323ee880ee35442",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286207,
  "host_pid": "9e6742732c60:1",
  "hash": "57f71f8701938799c851dbcdac9c0c3fcc06992fa7183251454265d1534c0ee1",
  "cid": "QmV157f71f8701938799c851dbcdac9c0c3fcc06992f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286207,
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
      "evaluated_at": 1760286207
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "2cb2e57b1b5904b522567adc0c2de6f76e87d42af3c551184acefad7810546f7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026545394
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': '1ef68d78d8cabe5b'}}}re': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': 'a9c92113e6dbf136'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 74, 'details': {'zscore': 3.46, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9144651}}}