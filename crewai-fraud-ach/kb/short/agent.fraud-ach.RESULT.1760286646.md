```json
{
  "id": "c10521a2fd23ffc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286646,
  "host_pid": "9e6742732c60:1",
  "hash": "68a42e28696d06a19e3cb1a42698999348c4e6250444e732692c2f5a9fa6cc98",
  "cid": "QmV168a42e28696d06a19e3cb1a42698999348c4e625",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286646,
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
      "evaluated_at": 1760286646
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
  "sig": "b5dd09f0b82bb673c651c45e185066ba32fd5d42fec3e24e8fb33a073022cf20"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 735962402542057
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14193600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285764, 'matching_hash': '8fcdc870d029f888'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '735962404', 'validation_error': 'Invalid routing number checksum'}}}