```json
{
  "id": "5714424e6cc15575",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286257,
  "host_pid": "9e6742732c60:1",
  "hash": "b465435049d32e1d63f2b38895285ed353973f75dee0f45fb77a44b4b1581a31",
  "cid": "QmV1b465435049d32e1d63f2b38895285ed353973f75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286257,
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
      "evaluated_at": 1760286257
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
  "sig": "d15a927cc8f38513193fc4c9452756e85e2bfb15e5035cb994592f532c67ae9c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462408143
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285765, 'matching_hash': '36407d3e627869a5'}}}