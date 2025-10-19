```json
{
  "id": "98bd7bbc539ea3c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286519,
  "host_pid": "9e6742732c60:1",
  "hash": "8edee044f59f05cc6f7e99d718ea856c040986a7c3bdb9665c6bc08414a9ea1e",
  "cid": "QmV18edee044f59f05cc6f7e99d718ea856c040986a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286519,
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
      "evaluated_at": 1760286519
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
  "sig": "b8c7a454566b920a98b5f390910aa71255ce896032469c8c423be295c53f0066"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009598152937
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285763, 'matching_hash': '12ca21f72ace6b8c'}}}