```json
{
  "id": "60797cce8d4677de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286094,
  "host_pid": "9e6742732c60:1",
  "hash": "1e74a25778fe14e8620ab8b52bf141e0c730a1523016a366a572eccf93cf1798",
  "cid": "QmV11e74a25778fe14e8620ab8b52bf141e0c730a152",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286094,
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
      "evaluated_at": 1760286094
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
  "sig": "881a21b0b47dd0cc4e9b4adff867563f016a79e4d15e0b3444dd95a953606844"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100271276448
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': '1d19524912ca559b'}}} 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760284979, 'matching_hash': 'fdbb68f6e232305a'}}}