```json
{
  "id": "ee92faec0292b8de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286042,
  "host_pid": "9e6742732c60:1",
  "hash": "4dd6dc7c299fa0ee51e3ed10b9a58a2e565263c33585c8d715a29411b669207e",
  "cid": "QmV14dd6dc7c299fa0ee51e3ed10b9a58a2e565263c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286042,
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
      "evaluated_at": 1760286042
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
  "sig": "ba90751b65e913ef6daa4e88292e1a8a40eed21d64154e597a1b6b97d6c38e5e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025341515
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285765, 'matching_hash': '76c6a410184ad94b'}}}