```json
{
  "id": "5b0fe0112d063101",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285482,
  "host_pid": "9e6742732c60:1",
  "hash": "d81c192ded0a911413c489a15f2043e249bf943ad4b3be0e2e7d5464561f02e3",
  "cid": "QmV1d81c192ded0a911413c489a15f2043e249bf943a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285482,
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
      "evaluated_at": 1760285482
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
  "sig": "221aa46a60e8c388e246921cc85542d48ceebc20b5db336a139e191a6b0fd03c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21069700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}