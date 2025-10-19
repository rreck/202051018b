```json
{
  "id": "028e82626c40bd1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286610,
  "host_pid": "9e6742732c60:1",
  "hash": "f7b22bfb548dbc705b75d6fcbb974f8086b3a71ce5f2e2db22f39ca56229e023",
  "cid": "QmV1f7b22bfb548dbc705b75d6fcbb974f8086b3a71c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286610,
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
      "evaluated_at": 1760286610
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
  "sig": "c55da1fda84beec6c02f5d36a79b41160a83ead481719efb2f7049299fdc0a2f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029384681
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285764, 'matching_hash': '45a3ccbce684d395'}}}