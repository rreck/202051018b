```json
{
  "id": "e202043257182a40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286469,
  "host_pid": "9e6742732c60:1",
  "hash": "781f2364926a5b9bc8045022d1d5db90020ec7c1dbbc2fe6f3f960161ad458c7",
  "cid": "QmV1781f2364926a5b9bc8045022d1d5db90020ec7c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286469,
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
      "evaluated_at": 1760286469
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
  "sig": "6bb7b4d148bc793bdee4f2ec1a597012931cdf5eb3664b571fd634c8b608fdad"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 735962402542057
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11532300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285764, 'matching_hash': '8fcdc870d029f888'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '735962404', 'validation_error': 'Invalid routing number checksum'}}}