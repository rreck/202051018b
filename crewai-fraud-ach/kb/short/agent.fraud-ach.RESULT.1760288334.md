```json
{
  "id": "e84a3d6b64678e92",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288334,
  "host_pid": "9e6742732c60:1",
  "hash": "74995b602146bf5c6177f3d35717386cdbd94773faa3eaf4fa4d80bb7931fa64",
  "cid": "QmV174995b602146bf5c6177f3d35717386cdbd94773",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288334,
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
      "evaluated_at": 1760288334
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
  "sig": "e2eaba5dd8735b3cd82ecb2a7bb093391e4144559c7358af9d35ba6da1b7ed72"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100275692414
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 496180170, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285764, 'matching_hash': '9e6182bea86cf2e1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5513113}}}