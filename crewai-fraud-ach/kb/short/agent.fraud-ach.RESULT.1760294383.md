```json
{
  "id": "541c064501699cc8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294383,
  "host_pid": "9e6742732c60:1",
  "hash": "c7b78718f42f63b48f7db3c01269002203d7366ce87d7eca10ce69c0b8479a32",
  "cid": "QmV1c7b78718f42f63b48f7db3c01269002203d7366c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294383,
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
      "evaluated_at": 1760294383
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
  "sig": "98749905f59f6f4ee472f4d4cdf5b562e12cd931659417d550f3dff8088503d2"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244890024234480
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 91048764, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'a93bcfd9fdd9d60c'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244890022', 'validation_error': 'Invalid routing number checksum'}}}