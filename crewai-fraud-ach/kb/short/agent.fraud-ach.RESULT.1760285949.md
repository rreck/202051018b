```json
{
  "id": "e68ab51fd3defc2a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285949,
  "host_pid": "9e6742732c60:1",
  "hash": "b2b04c7bd2117ca24399ae755fc36a0738e33bf222b95514e349a97de31e563c",
  "cid": "QmV1b2b04c7bd2117ca24399ae755fc36a0738e33bf2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285949,
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
      "evaluated_at": 1760285949
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
  "sig": "16794c1207cc50ff5ebd261f88529049e9b68ebf4fab02b4a1806122a5beb2b6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009596468860
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285763, 'matching_hash': 'e06c0748f018586e'}}}