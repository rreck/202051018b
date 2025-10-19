```json
{
  "id": "053c03e65630e4b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286526,
  "host_pid": "9e6742732c60:1",
  "hash": "f9af9b2aea124d434804764203e66460c8e6c81486dfa8097867a3f7b000b1e9",
  "cid": "QmV1f9af9b2aea124d434804764203e66460c8e6c814",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286526,
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
      "evaluated_at": 1760286526
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
  "sig": "5fe1f17025cbefb286c4f5278ffadbbd3e79725db38d43d398d0b407f5c4d0cb"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 870312149939109
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11173596, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285765, 'matching_hash': '2dbf2bb6cc4c52b4'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}