```json
{
  "id": "1500e63fb8b142d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292265,
  "host_pid": "9e6742732c60:1",
  "hash": "c3b330ff4034298431fac2a1e944351d1a72f6b3ca40fbb81570174051cf807d",
  "cid": "QmV1c3b330ff4034298431fac2a1e944351d1a72f6b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292265,
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
      "evaluated_at": 1760292265
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
  "sig": "04b9f0298cdb6c2d251d0e18bf5a0f5e8e6c5870cdb560e9302d2ab678239140"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241612576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 15070696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': 'a67f7546b45b9310'}}}