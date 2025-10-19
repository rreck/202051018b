```json
{
  "id": "d68074cdc952ea8a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288880,
  "host_pid": "9e6742732c60:1",
  "hash": "b9f153b74b0d86f2eaa5a2da433085d412cf451fd45df21bf3ccf5b6b45cca31",
  "cid": "QmV1b9f153b74b0d86f2eaa5a2da433085d412cf451f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288880,
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
      "evaluated_at": 1760288880
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
  "sig": "35b9022d3e0f7327b3dc1b2f284f133a7bc172408e4e9b40d0bc91534bda17ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595927429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 15471451, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': 'ad7b7e4988d8fb8c'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}