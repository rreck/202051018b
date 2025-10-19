```json
{
  "id": "79d46fc4edd02c59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286032,
  "host_pid": "9e6742732c60:1",
  "hash": "e43a0ba4b30189f5466a8d1a9f5589b075ca28f4e5d582254591625af9fcd053",
  "cid": "QmV1e43a0ba4b30189f5466a8d1a9f5589b075ca28f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286032,
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
      "evaluated_at": 1760286032
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
  "sig": "5092532a9907f5198e8ac1175dceff6df6a803b16ecec95f63be688a56f4e62b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000033554857
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285763, 'matching_hash': '1f36f93e880b57ba'}}}