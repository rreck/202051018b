```json
{
  "id": "aeb69928b6f7b8d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287074,
  "host_pid": "9e6742732c60:1",
  "hash": "e0c851c94e9bffb7e0d642036dd3587987dfeaab5567072fc63f5b87091c2c43",
  "cid": "QmV1e0c851c94e9bffb7e0d642036dd3587987dfeaab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287074,
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
      "evaluated_at": 1760287074
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
  "sig": "6102cecf4421a256626f030497375ee1c2a77300dab5bbf149963307986048f8"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 378944435908589
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11023709, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285763, 'matching_hash': '7919df3bb7d07869'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '378944430', 'validation_error': 'Invalid routing number checksum'}}}