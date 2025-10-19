```json
{
  "id": "a283ce1ccc6d7041",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286487,
  "host_pid": "9e6742732c60:1",
  "hash": "51490b42278a8cbb460a9b9a30a917da6903d767190d9ce663d59f63bee2e977",
  "cid": "QmV151490b42278a8cbb460a9b9a30a917da6903d767",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286487,
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
      "evaluated_at": 1760286487
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "47ae67fb3d23f28bcf08b15ef8a433532ec5c3f85292934dc42cb0356c489868"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 730896563459202
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285763, 'matching_hash': 'b6a475fea2d998c5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '730896563', 'validation_error': 'Invalid routing number checksum'}}}d': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5035466}}}