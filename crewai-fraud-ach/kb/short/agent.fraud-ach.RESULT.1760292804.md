```json
{
  "id": "d181a7d4504e9c46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292804,
  "host_pid": "9e6742732c60:1",
  "hash": "dbdfd6c1e7a360f3b66d276edea11d49c3a32df5e958eed47ece9ea8349f25f0",
  "cid": "QmV1dbdfd6c1e7a360f3b66d276edea11d49c3a32df5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292804,
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
      "evaluated_at": 1760292804
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
  "sig": "37d34b8051281c78a71893e6cc98845ed34935f1c1a031dc6a0832d9fae6fabf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464452578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 19742935, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285764, 'matching_hash': '0a8d6c8cd4d67655'}}}