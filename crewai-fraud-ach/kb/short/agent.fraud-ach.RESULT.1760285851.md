```json
{
  "id": "8c0c6ecae3ffe45c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285851,
  "host_pid": "9e6742732c60:1",
  "hash": "ad0242fefe1f3502f61d9c23f1102fbaf308e5a7d753eb0c8de895dc8b4204aa",
  "cid": "QmV1ad0242fefe1f3502f61d9c23f1102fbaf308e5a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285851,
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
      "evaluated_at": 1760285851
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
  "sig": "4d15448fbf10c1b7a702c4cff7fa54af1c19b0cde914daad7633c2c5c1d1617b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000025839448
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285765, 'matching_hash': 'a0edb6bd92ae1076'}}}