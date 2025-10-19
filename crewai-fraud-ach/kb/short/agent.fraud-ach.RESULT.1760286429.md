```json
{
  "id": "078f5b6f3ac11f37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286429,
  "host_pid": "9e6742732c60:1",
  "hash": "34dae42173dcdb0aa84613f08010caed4b51d393558985f6c6774bc93786f245",
  "cid": "QmV134dae42173dcdb0aa84613f08010caed4b51d393",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286429,
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
      "evaluated_at": 1760286429
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
  "sig": "4a7e5d944d6a11aa76dc2a181171b9001cfa0a9139227ac090653288e550d9dc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105152772165
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285764, 'matching_hash': '9371db7725d4e0a9'}}}