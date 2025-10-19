```json
{
  "id": "1d72c39300dae5b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285801,
  "host_pid": "9e6742732c60:1",
  "hash": "994808325b8864cd39a71e22be2365de5a2a533836a1748caf3ed22b796a9fa6",
  "cid": "QmV1994808325b8864cd39a71e22be2365de5a2a5338",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285801,
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
      "evaluated_at": 1760285801
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
  "sig": "149195e76d597d9d47205469ebb46d13f79f33cdec31e86f9ba600ad9336540c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105155063461
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285764, 'matching_hash': '55217e698cd3f78f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '728187403', 'validation_error': 'Invalid routing number checksum'}}}