```json
{
  "id": "d21d7f370c2e51f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760284989,
  "host_pid": "9e6742732c60:1",
  "hash": "d13dba03dc07420ceb5ba4a79b79861452cfa8babd8c59ffafd30d2cce352705",
  "cid": "QmV1d13dba03dc07420ceb5ba4a79b79861452cfa8ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760284989,
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
      "evaluated_at": 1760284989
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
  "sig": "d1130e113e59581295263d6443e1a008bac19299b2b9228d25b7ae76defcd2b8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000028775289
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760284979, 'matching_hash': 'c3a7255fa6117479'}}}