```json
{
  "id": "b4b6948fea87536b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288660,
  "host_pid": "9e6742732c60:1",
  "hash": "f41f6f1415dae18c73befa5fc3cb2c67debd6e846b14c23ad8c9f32279346729",
  "cid": "QmV1f41f6f1415dae18c73befa5fc3cb2c67debd6e84",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288660,
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
      "evaluated_at": 1760288660
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
  "sig": "bdf5901602136441e3bf17c0d4586b94b5b687a17b795cd207a1bab6df5c261a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598660548
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 22992900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': '4ba6ddd8e6715c89'}}}