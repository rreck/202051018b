```json
{
  "id": "f71d8814b882a2bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286406,
  "host_pid": "9e6742732c60:1",
  "hash": "0753845dde1d6c7e6c908dee58eac370e167d11a3c80141caea59fb645dafab5",
  "cid": "QmV10753845dde1d6c7e6c908dee58eac370e167d11a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286406,
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
      "evaluated_at": 1760286406
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
  "sig": "1fbb6a58370ab628b99ca66b341f93f2c05ad1ec4717fa533532500951ac3598"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 735962402542057
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10645200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285764, 'matching_hash': '8fcdc870d029f888'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '735962404', 'validation_error': 'Invalid routing number checksum'}}}