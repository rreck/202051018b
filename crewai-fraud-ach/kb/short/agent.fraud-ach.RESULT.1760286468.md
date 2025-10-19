```json
{
  "id": "275bde1ff6d999fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286468,
  "host_pid": "9e6742732c60:1",
  "hash": "43bc16bd60a07b3fce7e249e4d9ed309d97768f88195a2c49f7874cba8c1f9cf",
  "cid": "QmV143bc16bd60a07b3fce7e249e4d9ed309d97768f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286468,
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
      "evaluated_at": 1760286468
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
  "sig": "910c71691c4b61b4d2e5c41fa2fe4f21c437d8283c3db0facf45cce0e7d5721a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463568898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285764, 'matching_hash': '8016b691bce48ab1'}}}