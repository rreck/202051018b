```json
{
  "id": "f6e729f00bf45e68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286502,
  "host_pid": "9e6742732c60:1",
  "hash": "d3431b0bdd0ab87aa821d04f9ad92f8ef3731783b621071b1e7f6cb18e55cfca",
  "cid": "QmV1d3431b0bdd0ab87aa821d04f9ad92f8ef3731783",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286502,
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
      "evaluated_at": 1760286502
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
  "sig": "946ef2d4ff5b91038ee134841ed1cd763750a63a4b92185d9948f75c6346d21e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243684464
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285765, 'matching_hash': '4ae1f96c7cecc03b'}}}