```json
{
  "id": "ae0ce4dadeacc265",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291850,
  "host_pid": "9e6742732c60:1",
  "hash": "0a0312af9a6dbb808557429e18403952274f5b6457bd78dd77257dc80cd86911",
  "cid": "QmV10a0312af9a6dbb808557429e18403952274f5b64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291850,
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
      "evaluated_at": 1760291850
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
  "sig": "78c26c8afe85b648e0771bd3f9d4b5db6b8a1dea31b8623be04a7f1a1814244b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 57509384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}