```json
{
  "id": "75e7901778e36102",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288619,
  "host_pid": "9e6742732c60:1",
  "hash": "e52e4479b0275991f634e7f0b53bb3ff0a4646265d8458cb1b81b4926c0e24f3",
  "cid": "QmV1e52e4479b0275991f634e7f0b53bb3ff0a464626",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288619,
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
      "evaluated_at": 1760288619
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
  "sig": "a2f4027a1154249e41f9b0cc028a09eef7fe62b62d2ab4d9c4a0a19e66d593e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150128981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 18934740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': '59c56ba6c2207f9a'}}}