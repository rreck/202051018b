```json
{
  "id": "6fd59def32e6d9f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290381,
  "host_pid": "9e6742732c60:1",
  "hash": "0780c9f092775dacbed88e8ce8d4b1951351d276eb65acbdbbcccb3717fe43ca",
  "cid": "QmV10780c9f092775dacbed88e8ce8d4b1951351d276",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290381,
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
      "evaluated_at": 1760290381
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
  "sig": "8466f6faabdb54acea527d77b965579efbee149f13a14244e46c73201661953e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029877647
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 50832989, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': 'f76c4daf1b61ee5a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '730896563', 'validation_error': 'Invalid routing number checksum'}}}ds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9144651}}}