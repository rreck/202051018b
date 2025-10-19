```json
{
  "id": "7d200fb77f19f2d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290817,
  "host_pid": "9e6742732c60:1",
  "hash": "c15f947d3a7b007a5bd67c3bf78c2b33df2eaab0492308ebf309da6e4fd332ef",
  "cid": "QmV1c15f947d3a7b007a5bd67c3bf78c2b33df2eaab0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290817,
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
      "evaluated_at": 1760290817
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "ef0fe74a483573d929d74db09092fcee9b2c3b00a662db8e0968e11da1716aad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024843981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 23598720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285764, 'matching_hash': 'a5434e6981d8724b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '304701776', 'validation_error': 'Invalid routing number checksum'}}}