```json
{
  "id": "8707c91aeed6f5be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286165,
  "host_pid": "9e6742732c60:1",
  "hash": "7c687f2a2eefef4b520a7a26a8c4500bf35c33a47a6c3f5722113ed8e5af37a8",
  "cid": "QmV17c687f2a2eefef4b520a7a26a8c4500bf35c33a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286165,
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
      "evaluated_at": 1760286165
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
  "sig": "4410955bf63e9627d5f3d06fa524f3668a4a168860ded628d3d707eed14f642e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025329406
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285765, 'matching_hash': '4bb9b304f38123bb'}}}