```json
{
  "id": "f6088161f0e60d6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294824,
  "host_pid": "9e6742732c60:1",
  "hash": "0a59531328184f240965eef2b16bb7a1e9900128d5bd88d37412b203f868ad5a",
  "cid": "QmV10a59531328184f240965eef2b16bb7a1e9900128",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294824,
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
      "evaluated_at": 1760294824
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
  "sig": "cd50c614772940c37f4e0fc2e508fb6275a0434f3aa0e9242f2c3df8c9363912"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029354583
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 19437810, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'dbced9ae96be05e0'}}}