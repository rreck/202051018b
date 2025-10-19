```json
{
  "id": "c772e09098dd0ce7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292586,
  "host_pid": "9e6742732c60:1",
  "hash": "c4cbc94520fabe40ec8778e8ef657c97fab5604f946c7683acf9853bb007c4f8",
  "cid": "QmV1c4cbc94520fabe40ec8778e8ef657c97fab5604f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292586,
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
      "evaluated_at": 1760292586
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
  "sig": "ad22a45c664ab399bfc821ef5f565d57fea978f94323d1660f78cabd4bd877ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159149641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 38924856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '1bdba49a970d4caa'}}}