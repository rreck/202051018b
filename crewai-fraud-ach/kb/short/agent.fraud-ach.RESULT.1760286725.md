```json
{
  "id": "ec9b2475eb78ab1a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286725,
  "host_pid": "9e6742732c60:1",
  "hash": "e22937eece951eaeaaa6f8236edc48576e33574655415118a70c01f180a1e799",
  "cid": "QmV1e22937eece951eaeaaa6f8236edc48576e335746",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286725,
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
      "evaluated_at": 1760286725
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
  "sig": "d94bd4c9cadbe450799cb63b26d3a2db25a495400af3ecce23ac35bd56eab31c"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 118929074583077
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285765, 'matching_hash': '9c7c32bd8fa37035'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '118929079', 'validation_error': 'Invalid routing number checksum'}}}