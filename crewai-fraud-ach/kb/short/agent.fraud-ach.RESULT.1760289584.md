```json
{
  "id": "3686210afdbb2b33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289584,
  "host_pid": "9e6742732c60:1",
  "hash": "1a5da549326c3c295e3284c66f29b678902a40b4bb2488c92dde54a7d235a603",
  "cid": "QmV11a5da549326c3c295e3284c66f29b678902a40b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289584,
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
      "evaluated_at": 1760289584
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
  "sig": "fcb504032a2b6df97dc62eb0757faa7b9bfd54ef6e67d47575571144a26e2c6f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150676701
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 59786774, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': 'f947c72340b5e951'}}}