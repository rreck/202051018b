```json
{
  "id": "a5aaa0e2e8b2b4d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292116,
  "host_pid": "9e6742732c60:1",
  "hash": "39f8f4f5e476b96705e853e884cf08c5090bc727d6968707032ee16bbe14c11a",
  "cid": "QmV139f8f4f5e476b96705e853e884cf08c5090bc727",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292116,
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
      "evaluated_at": 1760292116
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
  "sig": "4dcc79815dfa877469e64a905df8fbc2d54ac6dbe457707b08c877d5b8964a89"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025339678
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 76686660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285765, 'matching_hash': '57e7473926bfe00b'}}}