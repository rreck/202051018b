```json
{
  "id": "38b8e7f075322adf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285432,
  "host_pid": "9e6742732c60:1",
  "hash": "9e29834f8b39117cf106796b82963b54c283b3df71da2d9792828cd2645f2509",
  "cid": "QmV19e29834f8b39117cf106796b82963b54c283b3df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285432,
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
      "evaluated_at": 1760285432
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
  "sig": "438db45b09b61539c0c4119638f52a0b7dc4b6e069b49706a2f43154774a16b3"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18962730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}