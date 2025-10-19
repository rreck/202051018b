```json
{
  "id": "52ed2a53d200d323",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286897,
  "host_pid": "9e6742732c60:1",
  "hash": "fdfcf22cc3bd9ba38f4ff17561343c286b8ce7dcccb3a96382cfdfeb6c42a82d",
  "cid": "QmV1fdfcf22cc3bd9ba38f4ff17561343c286b8ce7dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286897,
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
      "evaluated_at": 1760286897
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
  "sig": "6707cc35488f43ce693ba22c064784c87b521a6c45c1289d3c7c7dbf718eeb99"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000027363246
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285764, 'matching_hash': 'ed45becb5b65c89d'}}}