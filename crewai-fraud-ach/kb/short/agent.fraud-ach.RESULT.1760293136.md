```json
{
  "id": "4069d06d28721276",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293136,
  "host_pid": "9e6742732c60:1",
  "hash": "19325c47eb1ad115185f228074d8893a54a03f8896e32cca668e4571886064b9",
  "cid": "QmV119325c47eb1ad115185f228074d8893a54a03f88",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293136,
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
      "evaluated_at": 1760293137
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
  "sig": "89da213fca8f1b79d9d7432075f6db08e39afa59aba0f439eb2c3044db3e84b0"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 880809096286836
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 58849928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': 'c39e51142956e00e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '880809095', 'validation_error': 'Invalid routing number checksum'}}}