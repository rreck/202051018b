```json
{
  "id": "20da5dde9576512f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290057,
  "host_pid": "9e6742732c60:1",
  "hash": "43924f3e546e7285a541d7509409e6cc4eed32a0f95ec9968ac0e8ec15594a41",
  "cid": "QmV143924f3e546e7285a541d7509409e6cc4eed32a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290057,
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
      "evaluated_at": 1760290057
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
  "sig": "8d5586ce6bb84b0ea150ef304bea4b0655be20241bd3ed7f5baae7849c110b94"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467874144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 34885620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285764, 'matching_hash': '428cbf79813503ca'}}}