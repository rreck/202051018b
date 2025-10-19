```json
{
  "id": "efe37040f7f3c607",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292495,
  "host_pid": "9e6742732c60:1",
  "hash": "21f12eddb1c035f5e20b8403d9758d6cc50848e737fb1c8b491895e8e56be092",
  "cid": "QmV121f12eddb1c035f5e20b8403d9758d6cc50848e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292495,
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
      "evaluated_at": 1760292495
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
  "sig": "f07fc8405d59ff6f52d0d76d91dec5151afd75df248f6fc40b322f31ad4e3540"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274159227
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 24959376, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': 'c6403d45da933f2b'}}}