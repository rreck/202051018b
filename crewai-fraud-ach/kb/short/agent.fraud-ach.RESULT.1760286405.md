```json
{
  "id": "0292ff4f228fa616",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286405,
  "host_pid": "9e6742732c60:1",
  "hash": "a5315ef032105831ca5fe797436ecb4e0b8a93d6483ef3a77307def719dfae37",
  "cid": "QmV1a5315ef032105831ca5fe797436ecb4e0b8a93d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286405,
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
      "evaluated_at": 1760286405
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
  "sig": "16fd9081c661870b88ebd747109584a67b0bd00c41507d48cb1bb66bed39a5fe"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 683146203883533
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285764, 'matching_hash': '8f404d0fc37310f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '683146208', 'validation_error': 'Invalid routing number checksum'}}}