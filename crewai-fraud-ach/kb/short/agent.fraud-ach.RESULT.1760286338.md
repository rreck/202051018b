```json
{
  "id": "9ebe75a2ef3522e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286338,
  "host_pid": "9e6742732c60:1",
  "hash": "715d0b9a46a9042ca44f6adea18e8938e50c25fd12da0114e0c90b0930f5f7a8",
  "cid": "QmV1715d0b9a46a9042ca44f6adea18e8938e50c25fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286338,
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
      "evaluated_at": 1760286338
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
  "sig": "2b35bf60684e81a1aeeb786a441cc362f8a18a66a157a34c98351670e7c4aa4e"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 906924177607497
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285765, 'matching_hash': 'a0bedab775ea6194'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '906924178', 'validation_error': 'Invalid routing number checksum'}}}