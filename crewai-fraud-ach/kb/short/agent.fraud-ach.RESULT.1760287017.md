```json
{
  "id": "ce9720bf30f7b5b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287017,
  "host_pid": "9e6742732c60:1",
  "hash": "fa6702e99238e41d99687105acda63c950d7e8d54987d65a2d67a219b45378e6",
  "cid": "QmV1fa6702e99238e41d99687105acda63c950d7e8d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287017,
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
      "evaluated_at": 1760287017
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
  "sig": "6014ae47857f64bdf585a124fe6b37f972c13ba5a1788e6770f2262bcf716697"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000034778259
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285763, 'matching_hash': 'b6b775805828fc60'}}}