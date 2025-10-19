```json
{
  "id": "8a2d3ec511bdfac9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288395,
  "host_pid": "9e6742732c60:1",
  "hash": "c14b578c62d9da146f5e6616706814ee27918f221aa60e44d04930e2aeefdc3f",
  "cid": "QmV1c14b578c62d9da146f5e6616706814ee27918f22",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288395,
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
      "evaluated_at": 1760288395
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
  "sig": "48c457a485577323827f3b37a62523cc577583befe01c24fddae3d36e46e7a8c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 691661796885470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285764, 'matching_hash': 'c2d09785100b76ca'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}'validation_error': 'Invalid routing number checksum'}}}