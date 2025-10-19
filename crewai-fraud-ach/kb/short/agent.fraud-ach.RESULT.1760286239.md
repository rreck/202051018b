```json
{
  "id": "20dd40772617d5ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286239,
  "host_pid": "9e6742732c60:1",
  "hash": "5ccc2aba877133d51cd1f67c30738e86bab10a1856e7e354e990a00e53ff7096",
  "cid": "QmV15ccc2aba877133d51cd1f67c30738e86bab10a18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286239,
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
      "evaluated_at": 1760286239
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
  "sig": "8b1f0b7fbd549e232b95de18cb2aee3cba037cdf69a06826922fb95f94e1a7ac"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039326834
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285763, 'matching_hash': '4e66e6716d66a614'}}}