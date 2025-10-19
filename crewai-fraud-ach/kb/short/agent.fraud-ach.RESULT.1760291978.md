```json
{
  "id": "7c44bc0b928c72f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291978,
  "host_pid": "9e6742732c60:1",
  "hash": "be7ebe60d1c8746652fdc26d5447a1d541acaf165beeef57e961388bfd59e06e",
  "cid": "QmV1be7ebe60d1c8746652fdc26d5447a1d541acaf16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291978,
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
      "evaluated_at": 1760291978
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
  "sig": "0f1e6bcd6c4a59f80fc9204ccbccb52fc92c38ae5e41f397d1513766b491d79a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022218542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 75979783, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285765, 'matching_hash': 'd495c26a449690da'}}}