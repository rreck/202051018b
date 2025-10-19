```json
{
  "id": "8f1c99e62ed55df4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294376,
  "host_pid": "9e6742732c60:1",
  "hash": "92b7dcc49cd8a0bcde55696c99a71a2317d2eb6c8b4f9c879c41dcf9b4da4503",
  "cid": "QmV192b7dcc49cd8a0bcde55696c99a71a2317d2eb6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294376,
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
      "evaluated_at": 1760294376
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
  "sig": "1372b38e25bdca9564f72c5f1c48a36a2dcf3eeacad4d9f86ae9318181c1dfc5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023724402
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 56005707, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '3d4ab0f371876a2a'}}}