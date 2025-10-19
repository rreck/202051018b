```json
{
  "id": "3ab7339a31434134",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292239,
  "host_pid": "9e6742732c60:1",
  "hash": "f257ba7bc61e8368b3e2bcfb094a08c18e0b274c7d1d6e4eb3e9235281aad893",
  "cid": "QmV1f257ba7bc61e8368b3e2bcfb094a08c18e0b274c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292239,
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
      "evaluated_at": 1760292239
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
  "sig": "1899b1eeda7205af648194481ecff199bb33ad8e862165a5e69567acc19944b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024242004
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 48250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285764, 'matching_hash': '99660a13145cb677'}}}