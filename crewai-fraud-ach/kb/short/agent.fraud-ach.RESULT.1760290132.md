```json
{
  "id": "290d949d0069e3e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290132,
  "host_pid": "9e6742732c60:1",
  "hash": "e64ecb7baabadd0e6f75ecfaaf18a1b8a2ac5827571958be829ff3b0c95256ca",
  "cid": "QmV1e64ecb7baabadd0e6f75ecfaaf18a1b8a2ac5827",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290132,
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
      "evaluated_at": 1760290132
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
  "sig": "2234952f9c24706de8a4b8ef4cda97503d7acd2f018b840ff61634b57a2c91b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 61191634, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}