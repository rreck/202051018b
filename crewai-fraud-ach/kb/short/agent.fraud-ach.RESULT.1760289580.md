```json
{
  "id": "e8198762670dd0a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289580,
  "host_pid": "9e6742732c60:1",
  "hash": "4df2bd44fb1e1ec91e7d41933c2fb5fe2fde77be2122b15006dbddcb2c50d6ce",
  "cid": "QmV14df2bd44fb1e1ec91e7d41933c2fb5fe2fde77be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289580,
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
      "evaluated_at": 1760289580
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
  "sig": "3e09b09da03fb1ccb95d1bcca3a0b1ba8f8c91c1693fb17e763fa3d05770499c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029313979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 60023629, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': 'ee97e2abac1557d2'}}}