```json
{
  "id": "e838be72f448d4c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286492,
  "host_pid": "9e6742732c60:1",
  "hash": "23aaf9a10de7fac98d23b8dc258ca33b900714404e02c12ee94f2ab95781b591",
  "cid": "QmV123aaf9a10de7fac98d23b8dc258ca33b90071440",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286492,
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
      "evaluated_at": 1760286492
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
  "sig": "114e05776eb66dc31cd0b1456a8b3f6434cef150f6426b462e2283586be22143"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009592568865
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285763, 'matching_hash': 'ecded74c6845c7bc'}}}