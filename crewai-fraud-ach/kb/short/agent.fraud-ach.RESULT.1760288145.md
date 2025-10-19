```json
{
  "id": "c77d26aefa6ed451",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288145,
  "host_pid": "9e6742732c60:1",
  "hash": "0321802ef077934eb163d05a8f3cb50eebb09115ec336677eea155f6c8883a73",
  "cid": "QmV10321802ef077934eb163d05a8f3cb50eebb09115",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288145,
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
      "evaluated_at": 1760288145
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
  "sig": "6864637f6ffd5fd1dddc9b59ebbd69cd74c2f56978cb921c17da5a177451c3f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241124617
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 23217768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285763, 'matching_hash': 'fcf7fec38d983fba'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}