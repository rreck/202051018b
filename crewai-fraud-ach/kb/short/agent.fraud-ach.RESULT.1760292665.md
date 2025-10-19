```json
{
  "id": "04dd832e9160dd1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292665,
  "host_pid": "9e6742732c60:1",
  "hash": "8b566bbb78050628395087cf890cd02681a9a9daebaca54757fae0e5ad3accb4",
  "cid": "QmV18b566bbb78050628395087cf890cd02681a9a9da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292665,
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
      "evaluated_at": 1760292665
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
  "sig": "cdf7525218a6ef6594d1ff695262c84e1e4b6485fe2ca0149df2a031041f723b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279221197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 90197040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': '706f719d80b46657'}}}