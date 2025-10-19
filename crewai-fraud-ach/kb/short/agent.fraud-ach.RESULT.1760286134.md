```json
{
  "id": "4d5bea0bd27c0425",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286134,
  "host_pid": "9e6742732c60:1",
  "hash": "abc5c12469e4a79d4edb9a5e3dee64aba9922768f872763b1202f5cd63114be9",
  "cid": "QmV1abc5c12469e4a79d4edb9a5e3dee64aba9922768",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286134,
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
      "evaluated_at": 1760286134
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
  "sig": "c549d50d3f78b3c754b52a52660c36d8c62231ce94067f21d9b6afd591011bbc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105152525323
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285765, 'matching_hash': '867ad08c0d495d7b'}}}