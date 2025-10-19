```json
{
  "id": "817b03c340ed142e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286188,
  "host_pid": "9e6742732c60:1",
  "hash": "9f1086f56750bcab0dc2933dcb5c5ec5ff4a4fd76570231941be601d61ca74b1",
  "cid": "QmV19f1086f56750bcab0dc2933dcb5c5ec5ff4a4fd7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286188,
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
      "evaluated_at": 1760286188
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
  "sig": "63c358a4cf687a44a73c8c75af78f059c6a016d60add58050cbb5f611b2d7e71"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 044000033143138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 151319907, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285764, 'matching_hash': '6d0d609b65d243f3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.35, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8901171}}}