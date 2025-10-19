```json
{
  "id": "bfb1ba629cda407a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286679,
  "host_pid": "9e6742732c60:1",
  "hash": "993cbfdc89b4bd3da54a4104aa15b7b9dc4720f5c2902615733056ca78c41575",
  "cid": "QmV1993cbfdc89b4bd3da54a4104aa15b7b9dc4720f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286679,
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
      "evaluated_at": 1760286679
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
  "sig": "711bdec07b4a1ca7ad3f9196fb684ab79024f5b8f4d0d71d88ebe70523699813"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000038099532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13246926, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285765, 'matching_hash': 'ac68ba9e81a65c72'}}}