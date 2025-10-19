```json
{
  "id": "207735407d08953a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287138,
  "host_pid": "9e6742732c60:1",
  "hash": "da3c41ad8a0c4b8537d3be26df369e150c8a6138b9c72ebcb27931f85ac2682c",
  "cid": "QmV1da3c41ad8a0c4b8537d3be26df369e150c8a6138",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287138,
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
      "evaluated_at": 1760287138
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "36972365fdcbffa57d91acd08d5d7a9a2c1eaeac1ccce10ffa9fd9b3c5e33cdb"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000020143117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285765, 'matching_hash': '83c798d1c8d9cfec'}}}