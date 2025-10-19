```json
{
  "id": "4017f36fa24d8e7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286397,
  "host_pid": "9e6742732c60:1",
  "hash": "124ebac5b0b73c9f7932e0f9218ae31c7e5ef8db43681db799a9653a0aea76ed",
  "cid": "QmV1124ebac5b0b73c9f7932e0f9218ae31c7e5ef8db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286397,
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
      "evaluated_at": 1760286397
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
  "sig": "e83c0045ac95830fd7cb181129479f38f0e720c49e7015007db90c90b2eea7e4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242903308
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285764, 'matching_hash': '3fe1582345d32257'}}}