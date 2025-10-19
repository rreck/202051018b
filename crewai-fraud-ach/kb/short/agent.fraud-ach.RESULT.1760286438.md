```json
{
  "id": "6e88d20cf5a6c670",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286438,
  "host_pid": "9e6742732c60:1",
  "hash": "456967f1e3f9c8c97a9dbc0b9446726c9473db0fb851e84f178b2086134bd286",
  "cid": "QmV1456967f1e3f9c8c97a9dbc0b9446726c9473db0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286438,
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
      "evaluated_at": 1760286438
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
  "sig": "cb4641e3924450d125141a0b2e021521330fabc09d809878ddf8bfb7578ffdeb"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242075877
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285765, 'matching_hash': '7e39a816a4a44fcc'}}}