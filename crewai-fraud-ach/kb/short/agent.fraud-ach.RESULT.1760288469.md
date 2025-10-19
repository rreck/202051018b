```json
{
  "id": "3a9d7368236a44b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288469,
  "host_pid": "9e6742732c60:1",
  "hash": "0709b44a0d21f93be423aac33bf03db5a8689d890c9f89222b3739c79d471e1e",
  "cid": "QmV10709b44a0d21f93be423aac33bf03db5a8689d89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288469,
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
      "evaluated_at": 1760288469
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
  "sig": "b8ef428e459c9d6d9d6ff13add8409190949c85cd7853ddd02e4dffc659a6191"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271105789
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 25483588, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285764, 'matching_hash': 'b50c8d05dbdb14ee'}}}