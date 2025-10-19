```json
{
  "id": "11181475dd405d7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286000,
  "host_pid": "9e6742732c60:1",
  "hash": "56bd591c384220c2a8cb6c9927ec78c5c99c41a8f1fddae388d6b7445441b030",
  "cid": "QmV156bd591c384220c2a8cb6c9927ec78c5c99c41a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286000,
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
      "evaluated_at": 1760286000
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
  "sig": "a3bc95c62f8cef8f63548228c5c0170b2dc975a45777ff497c9d53e4b5b7864a"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 503193792297075
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285764, 'matching_hash': 'f478a6eb1bcd883b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '503193790', 'validation_error': 'Invalid routing number checksum'}}}