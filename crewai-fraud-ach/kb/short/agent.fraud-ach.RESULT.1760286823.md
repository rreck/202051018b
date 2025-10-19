```json
{
  "id": "39867ede02f6fdc0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286823,
  "host_pid": "9e6742732c60:1",
  "hash": "c0c405c5bfcbd43d0d025e798c6b85fef5a3b2a55a80f25e3329d5ce84ce3e88",
  "cid": "QmV1c0c405c5bfcbd43d0d025e798c6b85fef5a3b2a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286823,
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
      "evaluated_at": 1760286823
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
  "sig": "feb2d799ed078f4d8d996eceffe59c346d70fd57cdf2fff8add3491979d83dcb"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105153539871
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285765, 'matching_hash': '6120bfc166994b37'}}}