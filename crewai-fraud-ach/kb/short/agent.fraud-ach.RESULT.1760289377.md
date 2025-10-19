```json
{
  "id": "aa753b3659199599",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289377,
  "host_pid": "9e6742732c60:1",
  "hash": "d21ca5f000d178c2cf9903d44c312ca57ed505d57bb2e7510fe01fea064e9c0a",
  "cid": "QmV1d21ca5f000d178c2cf9903d44c312ca57ed505d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289377,
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
      "evaluated_at": 1760289377
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
  "sig": "e914ac8013f555964f76a857d296358b99c9f6c462c41f99dc40d18ba693aa0c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039495479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 49312824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285765, 'matching_hash': 'bbfd7bc59c80a282'}}}