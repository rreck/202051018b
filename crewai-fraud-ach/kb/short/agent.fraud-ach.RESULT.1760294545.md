```json
{
  "id": "32da2e8088b6e006",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294545,
  "host_pid": "9e6742732c60:1",
  "hash": "90dea360923f46295ed6931a6ef453d997e491faea06736c91ed9941ccb8e0a9",
  "cid": "QmV190dea360923f46295ed6931a6ef453d997e491fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294545,
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
      "evaluated_at": 1760294545
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
  "sig": "607eeea1b03c01865efe6aba8d10a4b5df904d88d2e99d9ea217ad561bd7f16a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024745112
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 14243280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'ff21c04b95925b18'}}}