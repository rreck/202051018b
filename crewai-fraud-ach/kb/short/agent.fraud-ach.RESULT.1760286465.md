```json
{
  "id": "ef481c9106ac0375",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286465,
  "host_pid": "9e6742732c60:1",
  "hash": "4677f4aeae6b95f3e680fbd7e648cc79e717677afcf11b5cbb20dadb0f8f8631",
  "cid": "QmV14677f4aeae6b95f3e680fbd7e648cc79e717677a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286465,
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
      "evaluated_at": 1760286465
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
  "sig": "5169227b2c3b0d415c5060daf729e471d290b3df497a54d7442542e173f26049"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000248710981
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': '9a1c8fb9d78dcf4a'}}}