```json
{
  "id": "aa4a3e137c9a1336",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286463,
  "host_pid": "9e6742732c60:1",
  "hash": "41475962a8c1a79fbb518ccf5af1daa0eb8e9f2cdc70969a7390e1dac78d3be3",
  "cid": "QmV141475962a8c1a79fbb518ccf5af1daa0eb8e9f2c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286463,
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
      "evaluated_at": 1760286463
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
  "sig": "e38e278f36ad611c9a82eedc22771957d3f5fa7ee94f64596906dc2ec99b41d6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009596811195
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285765, 'matching_hash': '0f37bc2cbfa5aec6'}}}