```json
{
  "id": "e882fd22d460d0d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287025,
  "host_pid": "9e6742732c60:1",
  "hash": "8e45b233427454c0d4c79114a2d93fca8253074b7d1ebf05ed0e3cb19f658d15",
  "cid": "QmV18e45b233427454c0d4c79114a2d93fca8253074b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287025,
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
      "evaluated_at": 1760287025
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
  "sig": "d52347f67c10e7d95679d49de21ecb13bef82be0594a92fec958b751810e5d39"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000035927231
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20876085, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285765, 'matching_hash': '0aeb814485d84e75'}}}