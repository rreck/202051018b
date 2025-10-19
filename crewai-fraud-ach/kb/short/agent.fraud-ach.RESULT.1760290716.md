```json
{
  "id": "98e410d9b97cbf37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290716,
  "host_pid": "9e6742732c60:1",
  "hash": "bcb7b4200dde0ba8dbae4e29f61910d0574740b85d18ab78f306731377300660",
  "cid": "QmV1bcb7b4200dde0ba8dbae4e29f61910d0574740b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290716,
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
      "evaluated_at": 1760290716
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
  "sig": "5af52bffb3a82026417bc5fbc086acc4c9ea388efbaa06a0367394e336d2c25d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 72029873, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}