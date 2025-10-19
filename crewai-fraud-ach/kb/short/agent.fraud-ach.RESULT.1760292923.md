```json
{
  "id": "4ed1a3e7b70ecd3d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292923,
  "host_pid": "9e6742732c60:1",
  "hash": "f14b8fa1a9edaa85aa66f79da12b7bb4a10c52b01fb0a45d6ac354af77c3a090",
  "cid": "QmV1f14b8fa1a9edaa85aa66f79da12b7bb4a10c52b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292923,
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
      "evaluated_at": 1760292923
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
  "sig": "4663c7374d65491f01cb5508aa4069b6264969687d4b16b03ff57fea8ca2e8fb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023536829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 28601872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': 'cf71240b8169078c'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '361190711', 'validation_error': 'Invalid routing number checksum'}}}