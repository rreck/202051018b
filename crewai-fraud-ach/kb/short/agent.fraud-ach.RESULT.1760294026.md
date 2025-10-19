```json
{
  "id": "26f6eb089e698f63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294026,
  "host_pid": "9e6742732c60:1",
  "hash": "cfee43dfcdde200d83e6e4b47fa4cf2650da0ce6b0cfe65d8b7ff03a0b3c1797",
  "cid": "QmV1cfee43dfcdde200d83e6e4b47fa4cf2650da0ce6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294026,
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
      "evaluated_at": 1760294026
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
  "sig": "f1152b53f3217ace8ded7adfe43ada5aede5d49335291697b60fb6227adf7281"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029230021
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 75321090, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': 'f06e706b59004f2f'}}}