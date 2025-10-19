```json
{
  "id": "2ab417947a25a337",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286651,
  "host_pid": "9e6742732c60:1",
  "hash": "5b7f90302c1ac8d210c690c86a797d9a497f8aa0fffa45083e326ceeee96ddeb",
  "cid": "QmV15b7f90302c1ac8d210c690c86a797d9a497f8aa0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286651,
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
      "evaluated_at": 1760286651
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8d64c0675508de5fe10ff96dd07ab7b1066be2eee8f19665644358b7e8801a69"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105155958228
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13489344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285765, 'matching_hash': '1e57f627a6d207f5'}}}