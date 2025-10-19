```json
{
  "id": "73cddd639b776eee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285888,
  "host_pid": "9e6742732c60:1",
  "hash": "a0966fa6b1ccdf68267462a7caa29b0cf9211d76f6ce74f392cabd94c5792d81",
  "cid": "QmV1a0966fa6b1ccdf68267462a7caa29b0cf9211d76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285888,
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
      "evaluated_at": 1760285888
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
  "sig": "f276fe42f525785ed7c0d760ee430dd2e82fc7af9fc548b378fb6e4c93f559a4"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 824845893834283
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285764, 'matching_hash': '751a36f41382ae06'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}