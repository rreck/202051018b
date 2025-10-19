```json
{
  "id": "5190f959bda30585",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291498,
  "host_pid": "9e6742732c60:1",
  "hash": "c48e8e6199f08db78a0669a7ffa70e0359418b588a39bd8d7001319d4998a54a",
  "cid": "QmV1c48e8e6199f08db78a0669a7ffa70e0359418b58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291498,
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
      "evaluated_at": 1760291498
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
  "sig": "891351a57cee52d90ba86623af9b8d69f17ff42a4d67818ee50c364ac132e00f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271105789
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 47713952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285764, 'matching_hash': 'b50c8d05dbdb14ee'}}}