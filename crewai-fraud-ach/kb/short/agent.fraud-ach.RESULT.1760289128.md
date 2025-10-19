```json
{
  "id": "a474f280f09fad0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289128,
  "host_pid": "9e6742732c60:1",
  "hash": "280b425246b470b9f19ad9c1110aebad0a9705493052f687f7ea06db29a5a046",
  "cid": "QmV1280b425246b470b9f19ad9c1110aebad0a970549",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289128,
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
      "evaluated_at": 1760289128
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
  "sig": "284dafba258c330c634437d903663fdf8f85b9c29e4d98928953891c53eb6a89"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 491975137325012
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 33594888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': '2178be3eb8984b5a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}