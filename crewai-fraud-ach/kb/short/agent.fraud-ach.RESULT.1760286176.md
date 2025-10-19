```json
{
  "id": "978d6a4adebbf4dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286176,
  "host_pid": "9e6742732c60:1",
  "hash": "5084a7cefea0cee8d87fefd8081490b040be30f1b0dbeb68fbfc6015715e2bee",
  "cid": "QmV15084a7cefea0cee8d87fefd8081490b040be30f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286176,
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
      "evaluated_at": 1760286176
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
  "sig": "91d201ce5c1cf448f6305a0d50160dd602f5c2aad5fed164175dae0ce7d04871"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000244267355
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285763, 'matching_hash': '9a2cfa03d6a38585'}}}