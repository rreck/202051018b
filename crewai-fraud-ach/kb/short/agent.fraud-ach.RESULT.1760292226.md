```json
{
  "id": "24c622a05cd6c0f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292226,
  "host_pid": "9e6742732c60:1",
  "hash": "5b11ee1c4cf6b389d261b2db237b39a2cfde4372034baf3949228ed74a269a2c",
  "cid": "QmV15b11ee1c4cf6b389d261b2db237b39a2cfde4372",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292226,
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
      "evaluated_at": 1760292226
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
  "sig": "3e0e847e6e1b9789dfe3606e8781e246cd6becdf7255142771331dd22195bcd4"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 036223731470664
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 59313725, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '119e459cb2bfe689'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '036223730', 'validation_error': 'Invalid routing number checksum'}}}