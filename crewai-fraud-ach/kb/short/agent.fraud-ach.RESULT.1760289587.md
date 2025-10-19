```json
{
  "id": "98804da73628af92",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289587,
  "host_pid": "9e6742732c60:1",
  "hash": "381929fb6781431162e4d55e08735100e8c9b592632b593ec6d5d423c77ebcb0",
  "cid": "QmV1381929fb6781431162e4d55e08735100e8c9b592",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289587,
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
      "evaluated_at": 1760289587
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
  "sig": "5438eb5b7cb2ae90d17288eb99dcbf83ebbc41bec2448bd7a772b9aedac8a44b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242521033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}