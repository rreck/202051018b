```json
{
  "id": "dc1881694077ca7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286835,
  "host_pid": "9e6742732c60:1",
  "hash": "375f82fa76721a06c0ba8c37c46431d936a4a708996ee02c71853ec290719aaf",
  "cid": "QmV1375f82fa76721a06c0ba8c37c46431d936a4a708",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286835,
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
      "evaluated_at": 1760286835
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
  "sig": "bd9c52ef4d42b938e4df102f5142cb17f45a03c67e7f5f01d3607109fecba7e9"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 580123061332551
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': 'b65f94a39c8828ce'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}d_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}