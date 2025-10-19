```json
{
  "id": "bb111b2eb2054de1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285783,
  "host_pid": "9e6742732c60:1",
  "hash": "08fe5d39875efe7244e7d321d724625fce6e5d3ef2fa27f0a463d14cc90d21d6",
  "cid": "QmV108fe5d39875efe7244e7d321d724625fce6e5d3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285783,
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
      "evaluated_at": 1760285783
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
  "sig": "3a283737ba725d30f0338775fc3871a066ad79046ac16c7f7e9f0ae8b551eff2"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 033505362547520
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285763, 'matching_hash': '3154a67bf8f8af44'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '033505362', 'validation_error': 'Invalid routing number checksum'}}}