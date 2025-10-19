```json
{
  "id": "34d02d1a1c4c917f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293474,
  "host_pid": "9e6742732c60:1",
  "hash": "3c7cc88aa6f62781da4cda95d02440d158b50a8bcfdc95a5ab48c2a7849b2de4",
  "cid": "QmV13c7cc88aa6f62781da4cda95d02440d158b50a8b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293474,
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
      "evaluated_at": 1760293474
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
  "sig": "b881987ec9288a93f1cd88cd918f8ed9b1fca458cd90b3f09b09963769564791"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037779899
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 90014913, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': '90378a324202fffb'}}}