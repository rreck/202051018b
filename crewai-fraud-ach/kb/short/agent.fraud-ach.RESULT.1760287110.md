```json
{
  "id": "e2dff7001582eeb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287110,
  "host_pid": "9e6742732c60:1",
  "hash": "f2486052e4d511a89d29b6fc5d3a87348c42563bb8406520f0547891c82aaa55",
  "cid": "QmV1f2486052e4d511a89d29b6fc5d3a87348c42563b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287110,
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
      "evaluated_at": 1760287110
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
  "sig": "84d0f555cfd0cfd0fa4160188a6e7335939c47f4870c008bd9387d096e91af40"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000027607406
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}