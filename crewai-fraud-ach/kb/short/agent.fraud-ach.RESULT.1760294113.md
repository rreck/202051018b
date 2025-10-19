```json
{
  "id": "79ec69093fd02b37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294113,
  "host_pid": "9e6742732c60:1",
  "hash": "65b089985d49bb694ded251c1c6c427ec9556ee49a0805ef0c9f18b29e527d21",
  "cid": "QmV165b089985d49bb694ded251c1c6c427ec9556ee4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294113,
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
      "evaluated_at": 1760294113
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
  "sig": "ef4db63e74a22cc4a0e7b2a4fa19584e57def36d02b15f28a79e9ff34e0debb0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027962561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 11600000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '3395f05250aaaeda'}}}