```json
{
  "id": "b90e4047ea24ed9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289674,
  "host_pid": "9e6742732c60:1",
  "hash": "ad3a4bdb5b7f6488dde379c6d0d4c9e13804bdd225a0aa85d93c9a9f4e9439fc",
  "cid": "QmV1ad3a4bdb5b7f6488dde379c6d0d4c9e13804bdd2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289674,
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
      "evaluated_at": 1760289674
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
  "sig": "6699bda7736aac3fffa456ab8e58201e5db9fbeac7f16b7a5f01a57e92b369a0"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 398958456380794
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 52640510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': 'e30dc560f8e3065a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}