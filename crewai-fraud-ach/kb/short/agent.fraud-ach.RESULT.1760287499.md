```json
{
  "id": "2250132a9ad7d817",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287499,
  "host_pid": "9e6742732c60:1",
  "hash": "919398db6322b96806fecb98e6b6efc5bbdd3bdf131f8ed9a4f36a4c5ce32ea0",
  "cid": "QmV1919398db6322b96806fecb98e6b6efc5bbdd3bdf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287499,
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
      "evaluated_at": 1760287499
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
  "sig": "80b85f9eaa543196a99a6700daf135267d287bb8209f9c43334ffa601283a282"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 021000025883497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 19716248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285765, 'matching_hash': '8c29ee71720a2634'}}}