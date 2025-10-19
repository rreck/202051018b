```json
{
  "id": "3dd0cecf29b912f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287122,
  "host_pid": "9e6742732c60:1",
  "hash": "20661ef41b1b9dbc9fa5b7548eaa8b81a9ee0ce527d6a6f33c8a9da1a221523b",
  "cid": "QmV120661ef41b1b9dbc9fa5b7548eaa8b81a9ee0ce5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287122,
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
      "evaluated_at": 1760287122
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
  "sig": "422bd1d1b62c276a2cd1dcbb794fe09ec2eb353bccb2e122b4df27d27616d2bf"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201465065641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 301912471, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285763, 'matching_hash': 'c71bd5f7fa32abe1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6161479}}}