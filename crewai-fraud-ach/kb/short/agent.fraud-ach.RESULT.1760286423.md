```json
{
  "id": "37d9fcaafe1a67c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286423,
  "host_pid": "9e6742732c60:1",
  "hash": "ac41832e787ce62d296ffe6575f9310144680967a3805da6a31aa6527f5217f8",
  "cid": "QmV1ac41832e787ce62d296ffe6575f9310144680967",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286423,
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
      "evaluated_at": 1760286423
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
  "sig": "8db6a362ac1698d22c948172858febd1f5acb1a15b2bd6a2f2facfab18aa0343"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000037990803
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': 'be616144f18eac0b'}}}