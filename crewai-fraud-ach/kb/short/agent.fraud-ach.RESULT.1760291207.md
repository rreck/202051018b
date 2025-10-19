```json
{
  "id": "a7a8503c40c36bea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291207,
  "host_pid": "9e6742732c60:1",
  "hash": "bafa67c3f065fc67d71b0b877f1379eb032f5b81821c5c2f3ed38fe6a4a68280",
  "cid": "QmV1bafa67c3f065fc67d71b0b877f1379eb032f5b81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291207,
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
      "evaluated_at": 1760291207
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
  "sig": "43f2f8717b60d4329d18e6ae751a5dd7213e7e3fb498ec55b48e2f131d025914"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592654855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 51028367, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285765, 'matching_hash': '0ed93ea6dd0046b6'}}}