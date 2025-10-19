```json
{
  "id": "e4534ae1acfef7d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292343,
  "host_pid": "9e6742732c60:1",
  "hash": "194e87a73c113b8404c7f2f4b1b1dd2e6dc10938fd85457538def463710d161e",
  "cid": "QmV1194e87a73c113b8404c7f2f4b1b1dd2e6dc10938",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292343,
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
      "evaluated_at": 1760292343
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
  "sig": "a3b1a0cdbc0a649aadd45c3f2c6cd6a5d240f7bd1a970350a28633f02c573be3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038480332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 14650545, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285765, 'matching_hash': '8289eea4583ef54f'}}}