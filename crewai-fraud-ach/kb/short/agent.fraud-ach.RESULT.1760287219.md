```json
{
  "id": "918bf840c37b48cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287219,
  "host_pid": "9e6742732c60:1",
  "hash": "33b7242451573e60c993763070b608ded121e988b4ee857fe59f93d8fddd213f",
  "cid": "QmV133b7242451573e60c993763070b608ded121e988",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287219,
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
      "evaluated_at": 1760287219
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
  "sig": "697eb8b525f0d86bc914174dc16ce7e90098e8942857f61e6b4807a759e3fc1c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105151957108
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 25066288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285765, 'matching_hash': 'c64e753eaec43197'}}}