```json
{
  "id": "8bfb4516c275d8d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286996,
  "host_pid": "9e6742732c60:1",
  "hash": "a5e77f657ebe3d7507d6b1dde54468d27a08d8015711dfd0b69f28a340f3f0cd",
  "cid": "QmV1a5e77f657ebe3d7507d6b1dde54468d27a08d801",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286996,
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
      "evaluated_at": 1760286996
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
  "sig": "333f22d2ccd21e4e23e971bc64da7f511121c163eb1c9faa2db0af82dd554ef0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241355402
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}