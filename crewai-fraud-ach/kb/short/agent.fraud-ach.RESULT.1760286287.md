```json
{
  "id": "a92cfe571e2b2a25",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286287,
  "host_pid": "9e6742732c60:1",
  "hash": "669e4c5fb46263452045acaf4b0ccd0c9cc88bc214a9248340f23e28a7afefbc",
  "cid": "QmV1669e4c5fb46263452045acaf4b0ccd0c9cc88bc2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286287,
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
      "evaluated_at": 1760286287
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
  "sig": "5ff0b178983f30e3d8e810362210a8b48db95cf11434cbd3e80e66bf7591d672"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469007601
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285765, 'matching_hash': '9208fda71b3c290c'}}}