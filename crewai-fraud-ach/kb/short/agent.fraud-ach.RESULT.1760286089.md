```json
{
  "id": "fa74e529c9c3fb99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286089,
  "host_pid": "9e6742732c60:1",
  "hash": "e33b8a6fa4f88acbdf1c1801707654efd56d46ba7fbd7d75a51c98a098013e4b",
  "cid": "QmV1e33b8a6fa4f88acbdf1c1801707654efd56d46ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286089,
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
      "evaluated_at": 1760286089
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
  "sig": "9cf140107ed50b3b513715993f4f4c3e1d638fcb61c2bb634111a11fbe7b24ab"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100274851410
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': '05e1730ec720465d'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '349235113', 'validation_error': 'Invalid routing number checksum'}}}': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6161479}}}