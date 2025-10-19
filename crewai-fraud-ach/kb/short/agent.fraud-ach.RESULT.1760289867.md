```json
{
  "id": "d34e4a62e527f8d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289867,
  "host_pid": "9e6742732c60:1",
  "hash": "b7d408147f128be6d827308a4f49e3ee39ba43bf5154a6498280c479e2ae1ce2",
  "cid": "QmV1b7d408147f128be6d827308a4f49e3ee39ba43bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289867,
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
      "evaluated_at": 1760289867
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
  "sig": "7936f8a7f174f2a1088c38746cddc6e7e323e98f95d7eb8e12f21bcd405fb1b7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278613406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 55621890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285765, 'matching_hash': 'bc206509fe1a9621'}}}