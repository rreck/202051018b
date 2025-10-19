```json
{
  "id": "594eaabf5c5e9233",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294128,
  "host_pid": "9e6742732c60:1",
  "hash": "b7e9254d5d5aaef7689e29283f46a268fc9c1570715ef2297189e0da2b54c68b",
  "cid": "QmV1b7e9254d5d5aaef7689e29283f46a268fc9c1570",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294128,
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
      "evaluated_at": 1760294128
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
  "sig": "a13dcdad3476886d84f88d3b737e8e9e3300a6ee0934ae8113ae826d87dc9b13"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 164661958921180
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 54321176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '1848c81652336fb1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '164661952', 'validation_error': 'Invalid routing number checksum'}}}