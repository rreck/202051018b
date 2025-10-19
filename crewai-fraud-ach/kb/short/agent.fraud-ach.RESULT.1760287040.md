```json
{
  "id": "b49bb0b8a913bed8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287040,
  "host_pid": "9e6742732c60:1",
  "hash": "5c8a6e6520a9a67389b787487220788f1bef64363892f184babb60d8abe06d12",
  "cid": "QmV15c8a6e6520a9a67389b787487220788f1bef6436",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287040,
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
      "evaluated_at": 1760287040
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
  "sig": "d972f84e8d837f9664aa456d6fe0103ea2076b3cd58aa517c81197e4c608dc8e"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 118929074583077
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10220510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': '9c7c32bd8fa37035'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '118929079', 'validation_error': 'Invalid routing number checksum'}}}