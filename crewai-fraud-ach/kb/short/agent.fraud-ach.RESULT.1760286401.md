```json
{
  "id": "43462eafc20b4a7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286401,
  "host_pid": "9e6742732c60:1",
  "hash": "362708ffc53cb8f0250f73e85fcc09f6989a8be41c864bdb94d1704cc1aa72ac",
  "cid": "QmV1362708ffc53cb8f0250f73e85fcc09f6989a8be4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286401,
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
      "evaluated_at": 1760286401
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
  "sig": "525b77f373d637c5e7926a0ea70e54da5664936c4c811ecd0637874d03416e29"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009590178584
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': 'edc4255e13a93cc1'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}