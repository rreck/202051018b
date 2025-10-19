```json
{
  "id": "45ce967d9eb928a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288378,
  "host_pid": "9e6742732c60:1",
  "hash": "125c3f44e31bb7cccc013480387dd8900d4bd52fcbb5fbb7f7f0eca65593ee51",
  "cid": "QmV1125c3f44e31bb7cccc013480387dd8900d4bd52f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288378,
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
      "evaluated_at": 1760288378
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
  "sig": "48039623daa6fb245d8e37ba2339a841123050c51f6e03bdb99595b16eb42cbb"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 507153179781967
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 19430502, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285765, 'matching_hash': 'b9dbbc4d232307f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '507153176', 'validation_error': 'Invalid routing number checksum'}}}