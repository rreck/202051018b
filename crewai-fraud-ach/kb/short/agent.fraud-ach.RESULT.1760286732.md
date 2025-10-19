```json
{
  "id": "ea09985104c7c46c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286732,
  "host_pid": "9e6742732c60:1",
  "hash": "5b7950f409dbedf5f7a658da68a64c8b381cb0af373700cfb4583b93dc4bce8a",
  "cid": "QmV15b7950f409dbedf5f7a658da68a64c8b381cb0af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286732,
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
      "evaluated_at": 1760286732
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
  "sig": "9b6f90b95fd11a235226cfaea4ffabd637cdfa971787321bca4cda7d892c2736"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 683146203883533
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13034770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285764, 'matching_hash': '8f404d0fc37310f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '683146208', 'validation_error': 'Invalid routing number checksum'}}}