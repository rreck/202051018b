```json
{
  "id": "a522b7bbe03bdcfd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286500,
  "host_pid": "9e6742732c60:1",
  "hash": "450ce02318826335b3ff2744d307fcd58290357b023a9b788bebeae50bd92a8e",
  "cid": "QmV1450ce02318826335b3ff2744d307fcd58290357b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286500,
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
      "evaluated_at": 1760286500
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
  "sig": "41f67fe23496f0c84edaee7dd6a03a8ad5ea819260294b0e626b491a69724658"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 009592678117470
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285764, 'matching_hash': 'f5249213623024b2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '009592679', 'validation_error': 'Invalid routing number checksum'}}}