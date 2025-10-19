```json
{
  "id": "63f1abd5f198f904",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292474,
  "host_pid": "9e6742732c60:1",
  "hash": "22ec74e7e64961a14dd46b252927f6892f95e5b232e191cf8b4ed4218dabc7b4",
  "cid": "QmV122ec74e7e64961a14dd46b252927f6892f95e5b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292474,
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
      "evaluated_at": 1760292474
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
  "sig": "9cdbd907614045503e10670c7c3370003af91fab883b564db41e8911480c6111"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462125361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 34693758, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285764, 'matching_hash': '410e2c6110d1d339'}}}