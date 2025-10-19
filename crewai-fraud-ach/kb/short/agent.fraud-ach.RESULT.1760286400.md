```json
{
  "id": "3bd1f11ae484384d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286400,
  "host_pid": "9e6742732c60:1",
  "hash": "3e48b388cfcf920b5eb84b732f0372a87aa72d98591d5262dce555882584e68b",
  "cid": "QmV13e48b388cfcf920b5eb84b732f0372a87aa72d98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286400,
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
      "evaluated_at": 1760286401
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
  "sig": "f646c2e036fd2ec99b9e1431680bba6cd6081ba79a65ae1e2346adcf2f480d3a"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 818309298369568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11306640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285765, 'matching_hash': '9e3984c977816ea5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}