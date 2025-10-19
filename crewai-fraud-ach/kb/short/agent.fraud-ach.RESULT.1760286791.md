```json
{
  "id": "e1fccf92d2e0c012",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286791,
  "host_pid": "9e6742732c60:1",
  "hash": "ded5084e22aa80eb51d48c379294a80bf815c6997a7dd26a7ec4504733cb403c",
  "cid": "QmV1ded5084e22aa80eb51d48c379294a80bf815c699",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286791,
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
      "evaluated_at": 1760286791
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
  "sig": "2008e0b3f825414d77afb00f5eeb6590bb6bd202ab7dfb2d90536c50c85568d5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029441717
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285764, 'matching_hash': 'f6bac04718607b3a'}}}