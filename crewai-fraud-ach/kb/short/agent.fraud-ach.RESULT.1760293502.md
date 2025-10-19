```json
{
  "id": "61bea986316dce21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293502,
  "host_pid": "9e6742732c60:1",
  "hash": "e7aa2c96681cdcc6ea9fef16bfd970a63028429a90db37809e59c2b76d96519c",
  "cid": "QmV1e7aa2c96681cdcc6ea9fef16bfd970a63028429a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293502,
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
      "evaluated_at": 1760293502
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
  "sig": "1903000a2ae5e15e30e4188e44e2006512315bddb1066b19f0b51ab08e8076e7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 294015856728576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 106295200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '68167a889af65895'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '294015854', 'validation_error': 'Invalid routing number checksum'}}}