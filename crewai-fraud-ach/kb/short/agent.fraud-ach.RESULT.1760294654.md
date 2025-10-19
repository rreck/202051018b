```json
{
  "id": "4e52d73b224d5425",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294654,
  "host_pid": "9e6742732c60:1",
  "hash": "0fbc8a2175571dd0b0a42fb8c875652492900bf556605b303d4c77ed68e9cf52",
  "cid": "QmV10fbc8a2175571dd0b0a42fb8c875652492900bf5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294654,
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
      "evaluated_at": 1760294654
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
  "sig": "80c8faf9cbbaf03b5cfc443ad5d4ccb89d56417f93542bdc86e1a60624df5582"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240263900
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 60500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285764, 'matching_hash': 'e5d68d31887f65d4'}}}