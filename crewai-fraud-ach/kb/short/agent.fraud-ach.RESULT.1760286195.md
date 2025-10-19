```json
{
  "id": "0667e10a6a77f432",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286195,
  "host_pid": "9e6742732c60:1",
  "hash": "a852a37ddcb3239dde0f72ac277fc287e86acbe84445d4f96b95a732f85265ec",
  "cid": "QmV1a852a37ddcb3239dde0f72ac277fc287e86acbe8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286195,
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
      "evaluated_at": 1760286195
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
  "sig": "f930563318174b59d7ea2c83fce9cb742344cc368d6bfd4573e2fadf8b74b82c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039495479
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285765, 'matching_hash': 'bbfd7bc59c80a282'}}}