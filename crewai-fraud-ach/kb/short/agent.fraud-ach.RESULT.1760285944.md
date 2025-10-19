```json
{
  "id": "078939a4c389050b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285944,
  "host_pid": "9e6742732c60:1",
  "hash": "12b4dae48706e457a168410a9a307bced4cf1fd264ec4d239c3eb090f7ef8a90",
  "cid": "QmV112b4dae48706e457a168410a9a307bced4cf1fd2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285944,
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
      "evaluated_at": 1760285944
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
  "sig": "cfaf4d53bf4601f99bcf93d44ad8f437fcc338c9c1c4d702888fa317ddd2958d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000030595065
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285763, 'matching_hash': '3889a0f66c8870f8'}}}re': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285764, 'matching_hash': '9e6182bea86cf2e1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5513113}}}