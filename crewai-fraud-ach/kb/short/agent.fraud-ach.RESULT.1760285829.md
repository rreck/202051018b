```json
{
  "id": "a007cb10a1c05aaf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285829,
  "host_pid": "9e6742732c60:1",
  "hash": "672d29aff8051c2337e58d7191bd722f6e05b77629370a5bc1ccf4781a864259",
  "cid": "QmV1672d29aff8051c2337e58d7191bd722f6e05b776",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285829,
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
      "evaluated_at": 1760285829
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
  "sig": "b56afaba3f3b9950ce55447eb5809db53a7c63345578cefbfe33a352050f636c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201466702370
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285765, 'matching_hash': 'c2e86be7e57e9a06'}}}