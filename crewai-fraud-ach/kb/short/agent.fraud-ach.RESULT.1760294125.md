```json
{
  "id": "157646486e8e6d27",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294125,
  "host_pid": "9e6742732c60:1",
  "hash": "1d7749c6caf80e93e862c0053a1ccad52042e891e9a898dd5476dac99ba874c8",
  "cid": "QmV11d7749c6caf80e93e862c0053a1ccad52042e891",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294125,
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
      "evaluated_at": 1760294125
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
  "sig": "2be2943b3fe8ca14067aab2382faaa0d7c6f58ef771d4cd99019a46abf1328de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021479776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 53484352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '6c002fd60c3e5dde'}}}}