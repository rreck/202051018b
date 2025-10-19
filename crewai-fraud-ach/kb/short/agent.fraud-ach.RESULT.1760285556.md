```json
{
  "id": "1fbbb6d8d6c6bce7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285556,
  "host_pid": "9e6742732c60:1",
  "hash": "80d8041b14a7b8e512f5037def1332d30599946aeefe89e85cdf89d03cbc8e75",
  "cid": "QmV180d8041b14a7b8e512f5037def1332d30599946a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285556,
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
      "evaluated_at": 1760285556
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
  "sig": "0e7f018e720054e71bca9f16601a32ecee90ad3a9274390949c46507ba5f92fd"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000247969582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 28203201, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760284979, 'matching_hash': '259c183eb9552f9c'}}}