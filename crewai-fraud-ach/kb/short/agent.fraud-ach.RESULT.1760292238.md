```json
{
  "id": "1202ed04c6aca0ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292238,
  "host_pid": "9e6742732c60:1",
  "hash": "4c83035f7eeb292249f77d9101652bc41e473e8101c48447f789fed7ad5af3fa",
  "cid": "QmV14c83035f7eeb292249f77d9101652bc41e473e81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292238,
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
      "evaluated_at": 1760292238
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
  "sig": "510e1748abf1105d0d85c7b8651f4781da17c20c9392d2d19176af5f3d536a79"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022844283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 269, 'threshold': 50, 'total_amount': 50672875, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 268, 'first_seen': 1760284979, 'matching_hash': '9c963f39e9fb9122'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}