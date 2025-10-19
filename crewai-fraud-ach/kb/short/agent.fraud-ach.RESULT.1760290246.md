```json
{
  "id": "f6ce9b61bf2d9a5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290246,
  "host_pid": "9e6742732c60:1",
  "hash": "a7fcc6906e0d6397fb4106c2227d83db4fb21a5b1e964150645cc2308c98f45a",
  "cid": "QmV1a7fcc6906e0d6397fb4106c2227d83db4fb21a5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290246,
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
      "evaluated_at": 1760290246
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
  "sig": "50c68b77bd9980008054bef73eaa6c7bb20d08b896db7818fac5a62ab36f84b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462125361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 25407045, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285764, 'matching_hash': '410e2c6110d1d339'}}}