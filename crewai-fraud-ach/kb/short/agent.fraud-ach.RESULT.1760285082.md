```json
{
  "id": "76c665d4ad24f055",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285082,
  "host_pid": "9e6742732c60:1",
  "hash": "aadd8c33e5191c851b90f714f457f82ad5fa76f572fb8505a772be8e6ab18c41",
  "cid": "QmV1aadd8c33e5191c851b90f714f457f82ad5fa76f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285082,
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
      "evaluated_at": 1760285082
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
  "sig": "d3549b55165d65b51708d319036712ccbdbf4ea8d7849675ca6cffe206d65ada"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}