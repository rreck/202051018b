```json
{
  "id": "aaf6c348980e7582",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286434,
  "host_pid": "9e6742732c60:1",
  "hash": "941c600ce54a6181ff2dcc2590729d215db9e1c2a7cf2b8cd783d100bcd4b925",
  "cid": "QmV1941c600ce54a6181ff2dcc2590729d215db9e1c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286434,
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
      "evaluated_at": 1760286434
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
  "sig": "3980f83fa1ac67709ffe1ed06da271a5f5d8177a7ee5578cf3875d8945f5d773"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100274747147
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': '9bf7edfe04e96377'}}}