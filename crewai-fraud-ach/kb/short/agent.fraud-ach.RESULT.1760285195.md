```json
{
  "id": "d16191779492b981",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285195,
  "host_pid": "9e6742732c60:1",
  "hash": "eafb51bdd564ae5d288dde15f4724ce53a57181fb78c1477c26f1c2c441f4b37",
  "cid": "QmV1eafb51bdd564ae5d288dde15f4724ce53a57181f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285195,
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
      "evaluated_at": 1760285195
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
  "sig": "b0dd0ff2e0307af271a623235ad355f3a9579547388ad8a90ae6f50bb746fed6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}