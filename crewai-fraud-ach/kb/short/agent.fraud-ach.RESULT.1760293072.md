```json
{
  "id": "a886edd4573b9122",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293072,
  "host_pid": "9e6742732c60:1",
  "hash": "36cbfe7e04305f97111d96d4438a0f0bb09823a75834a2324853dbafe2e02591",
  "cid": "QmV136cbfe7e04305f97111d96d4438a0f0bb09823a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293072,
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
      "evaluated_at": 1760293072
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
  "sig": "a0f8c69679eed807d55befd5ac91a06d15dcfc3f4d9181162a4f869492a14fa4"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244890024234480
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 81060292, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': 'a93bcfd9fdd9d60c'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244890022', 'validation_error': 'Invalid routing number checksum'}}}