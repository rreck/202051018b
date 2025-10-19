```json
{
  "id": "7ee620b1d173f7b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286736,
  "host_pid": "9e6742732c60:1",
  "hash": "7de887d959720358c329ffa0a3909c7efae32d6d4e01543e6e53ac531272b73e",
  "cid": "QmV17de887d959720358c329ffa0a3909c7efae32d6d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286736,
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
      "evaluated_at": 1760286736
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
  "sig": "0b721593884a96624769fa9e9e79b66196307a5607f953bd2619c0e856d35ed3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000034020503
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285765, 'matching_hash': '8db66b2beb557931'}}}