```json
{
  "id": "8cde969022e77d53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287447,
  "host_pid": "9e6742732c60:1",
  "hash": "85e65a4fe6a74772e916a6370d3fe1a520a7e9ff17faa6d4c664a6f8a64f22d0",
  "cid": "QmV185e65a4fe6a74772e916a6370d3fe1a520a7e9ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287447,
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
      "evaluated_at": 1760287447
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
  "sig": "6938b5cf71ad0b48d0c8ed21a94102e45e87040a43131dff33bd972955c4ec19"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000025001530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 14487240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285765, 'matching_hash': 'c7ad70870577ca51'}}}