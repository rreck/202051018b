```json
{
  "id": "9147a4648a5e5eb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286929,
  "host_pid": "9e6742732c60:1",
  "hash": "95defc79b6c5c1622bae280147ec86ce4dc3c1b060e2400dd033415a63ce931f",
  "cid": "QmV195defc79b6c5c1622bae280147ec86ce4dc3c1b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286929,
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
      "evaluated_at": 1760286929
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
  "sig": "fed4a463773d0a86ff68de9e18d1ddabd0e7db7dbf2b15b7e1c0200e514886e3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240751710
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285763, 'matching_hash': 'c9609c1b2bce9c12'}}}