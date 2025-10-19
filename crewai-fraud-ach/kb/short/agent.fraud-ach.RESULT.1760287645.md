```json
{
  "id": "4df5b48b5ec8ec9e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287645,
  "host_pid": "9e6742732c60:1",
  "hash": "91b85a5c3f6bf431fc709c4de9c8d21a6d809c406f6eab123bc036ef8c46e8fa",
  "cid": "QmV191b85a5c3f6bf431fc709c4de9c8d21a6d809c40",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287645,
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
      "evaluated_at": 1760287645
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
  "sig": "02d78b573938e69ad0d5b1e44c75de67d6dead313369b6f4d714a97aa2c1d18b"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 111000028970082
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 19006225, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285765, 'matching_hash': 'a98af89fc7548453'}}}