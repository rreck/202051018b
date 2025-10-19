```json
{
  "id": "e379fa3e788f6a0f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292390,
  "host_pid": "9e6742732c60:1",
  "hash": "d422f0163a0bdd97d571479cc0aceee92bfd4b3a950e0fe241aac6c69f317e71",
  "cid": "QmV1d422f0163a0bdd97d571479cc0aceee92bfd4b3a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292390,
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
      "evaluated_at": 1760292390
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
  "sig": "8867615e36bee854dc67dd7bc238f3120842ac4c8220112c437b16a41aff8bb5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 507153179781967
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 41850312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': 'b9dbbc4d232307f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '507153176', 'validation_error': 'Invalid routing number checksum'}}}