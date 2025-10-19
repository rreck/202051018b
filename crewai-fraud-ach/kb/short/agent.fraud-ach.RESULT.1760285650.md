```json
{
  "id": "ab16e685185e48de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285650,
  "host_pid": "9e6742732c60:1",
  "hash": "56d50a81afeaae5e7a8628255fabd38cdf7f99b3def6b2d98b646eb55d6ef0ab",
  "cid": "QmV156d50a81afeaae5e7a8628255fabd38cdf7f99b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285650,
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
      "evaluated_at": 1760285650
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
  "sig": "9e5aeec1b4c41460657a3756c1e4426d07a21ae6be8b81166269bcb1c99d95f3"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 27812004, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}