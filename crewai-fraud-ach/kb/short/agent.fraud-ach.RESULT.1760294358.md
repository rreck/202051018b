```json
{
  "id": "b4ac5c8d42f5ff4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294358,
  "host_pid": "9e6742732c60:1",
  "hash": "b13896e4df331dcbb38f2f5764070bad611b9c7e67c91c21c812113b88d04e6e",
  "cid": "QmV1b13896e4df331dcbb38f2f5764070bad611b9c7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294358,
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
      "evaluated_at": 1760294358
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
  "sig": "2ecb147b21f7076d8f44f0f9f4acb4dd4029774856a57e621ebc427e71e601c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463882943
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 29265888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}