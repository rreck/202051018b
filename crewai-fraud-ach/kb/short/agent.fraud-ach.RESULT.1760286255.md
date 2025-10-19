```json
{
  "id": "f8b4d71c37e313d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286255,
  "host_pid": "9e6742732c60:1",
  "hash": "b981f7e3fd8fa17c7c4b073047f9973eb4a8c2e4539e4760f6e9e6dfa87944aa",
  "cid": "QmV1b981f7e3fd8fa17c7c4b073047f9973eb4a8c2e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286255,
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
      "evaluated_at": 1760286255
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
  "sig": "268995f3502d15c7148dadbdb0f1971366b94feba978e1db56de62b762f082a5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105159928324
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285765, 'matching_hash': 'f9e49b53b0020755'}}}