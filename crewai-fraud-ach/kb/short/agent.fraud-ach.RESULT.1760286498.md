```json
{
  "id": "9467698837277fb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286498,
  "host_pid": "9e6742732c60:1",
  "hash": "8edd97ecdfd3ddeb18c8d2c33c85832c580a56f4c1d7a9efce1d042a2e533de9",
  "cid": "QmV18edd97ecdfd3ddeb18c8d2c33c85832c580a56f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286498,
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
      "evaluated_at": 1760286498
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
  "sig": "630665947d85d416631fba0da7c780ebb1ed154900be63d7052bccdc54d0db01"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 063100275328879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 151327602, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285764, 'matching_hash': '9f5415d10b328afc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5604726}}}