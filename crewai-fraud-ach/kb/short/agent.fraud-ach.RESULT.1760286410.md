```json
{
  "id": "6f3af78c032d4d24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286410,
  "host_pid": "9e6742732c60:1",
  "hash": "24025dbe0df0e262d2bd40d8c1563ff4c6c858a268376a4fda4264d3e29db080",
  "cid": "QmV124025dbe0df0e262d2bd40d8c1563ff4c6c858a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286410,
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
      "evaluated_at": 1760286410
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
  "sig": "2165adc81243d97e35187efafed56a073a53e32ad3cb268af5c4da77b428db85"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242521033
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}