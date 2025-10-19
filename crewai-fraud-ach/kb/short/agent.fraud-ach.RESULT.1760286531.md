```json
{
  "id": "4b62d70da4bf46fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286531,
  "host_pid": "9e6742732c60:1",
  "hash": "34627d817dd4c5df6d3a3949ef53599b0be73589095e268b0fa5234d7e938461",
  "cid": "QmV134627d817dd4c5df6d3a3949ef53599b0be73589",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286531,
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
      "evaluated_at": 1760286531
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
  "sig": "cdd45098bc5813242e9207a7a3bb99dd5464bd445024bdd23622f9eeb4727333"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105154024479
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285765, 'matching_hash': 'af946edf21c4a5d6'}}}