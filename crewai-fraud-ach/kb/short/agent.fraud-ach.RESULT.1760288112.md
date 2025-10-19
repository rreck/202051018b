```json
{
  "id": "d9bfbd4062884e20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288112,
  "host_pid": "9e6742732c60:1",
  "hash": "e9004d3e77b77f5b58086edd6e175309ae0d3f5241170642d983a639c17c7cf1",
  "cid": "QmV1e9004d3e77b77f5b58086edd6e175309ae0d3f52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288112,
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
      "evaluated_at": 1760288112
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "9dd3fa1559364546f67a02cc3b21c06b8e08f919d4f92c3ab42131e201e38fab"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 111000022658248
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 778588970, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285764, 'matching_hash': '6b9326523c35dc7b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.57, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9380590}}}