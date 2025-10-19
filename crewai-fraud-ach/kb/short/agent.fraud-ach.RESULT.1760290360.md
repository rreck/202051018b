```json
{
  "id": "87f1a613f4ccb049",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290360,
  "host_pid": "9e6742732c60:1",
  "hash": "fe054246205d9205b24a7e93750d54f9500e50f2c691da2ff13a9e0e67588ee0",
  "cid": "QmV1fe054246205d9205b24a7e93750d54f9500e50f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290360,
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
      "evaluated_at": 1760290360
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
  "sig": "0f7a2b240555d80d8cd440c86eaeb51eadfb295774432329c50d97d52640f4c6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 491975137325012
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 43614416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '2178be3eb8984b5a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}