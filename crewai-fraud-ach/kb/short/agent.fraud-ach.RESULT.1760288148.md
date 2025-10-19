```json
{
  "id": "fead720cd3bd5341",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288148,
  "host_pid": "9e6742732c60:1",
  "hash": "68a92d3eefa7fca3bb1901e83653a944ae9e956f6a9d834a00aea051d2e5a579",
  "cid": "QmV168a92d3eefa7fca3bb1901e83653a944ae9e956f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288148,
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
      "evaluated_at": 1760288148
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
  "sig": "fe9c3ecac1c4d7f763d5fdb017cb1902b31b6e9c798fcf93e2a8f4410a893a81"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 880809096286836
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 23317896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285765, 'matching_hash': 'c39e51142956e00e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '880809095', 'validation_error': 'Invalid routing number checksum'}}}