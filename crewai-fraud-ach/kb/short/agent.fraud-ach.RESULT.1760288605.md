```json
{
  "id": "09853700ab3a61d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288605,
  "host_pid": "9e6742732c60:1",
  "hash": "df94ffd50ab11bbf49b8eddfd899b62ec1dea4f2c3983ad174a520264fceffc6",
  "cid": "QmV1df94ffd50ab11bbf49b8eddfd899b62ec1dea4f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288605,
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
      "evaluated_at": 1760288605
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
  "sig": "c1471d74dfe4481221d0d54280edc245e57b0edb2fe5f69ed9a4444d558fcbe7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 107455396447712
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 48721484, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285765, 'matching_hash': 'bb26c320d6c9a382'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '107455391', 'validation_error': 'Invalid routing number checksum'}}}