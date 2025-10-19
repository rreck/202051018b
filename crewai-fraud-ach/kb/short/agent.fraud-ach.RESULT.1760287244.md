```json
{
  "id": "be31bb7b46395123",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287244,
  "host_pid": "9e6742732c60:1",
  "hash": "8eeb710956ad2f9e14aa7384fb5348cd6485a8e01edda831d9a56b5233019371",
  "cid": "QmV18eeb710956ad2f9e14aa7384fb5348cd6485a8e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287244,
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
      "evaluated_at": 1760287244
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
  "sig": "3776186c93369d5656f1d261d5723df5789efc7835b8caadd14d100995a2a26d"
}
```

Fraud detected: duplicate_transaction (score: 70)
Transaction: 031201468284841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 56, 'details': {'transaction_count': 53, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285764, 'matching_hash': 'af26bab6e9f38d2a'}}}