```json
{
  "id": "fc7c0918d2c1502c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291693,
  "host_pid": "9e6742732c60:1",
  "hash": "b4a6f6c0b71f51b6ddaee85d19d61ec2182cf0ffbfd8793d1adaec2a53aa99b8",
  "cid": "QmV1b4a6f6c0b71f51b6ddaee85d19d61ec2182cf0ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291693,
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
      "evaluated_at": 1760291693
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
  "sig": "8c189e98aafe0bf5c6d7e5257783822c098999308cdbac8a170305cba3018d0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274851410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 22403818, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '05e1730ec720465d'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '349235113', 'validation_error': 'Invalid routing number checksum'}}}