```json
{
  "id": "b2c33115c829b87c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286161,
  "host_pid": "9e6742732c60:1",
  "hash": "dbc4cff6db28e1eeeeb05c78c37776bb376db462ced5ef6167933a3069d326f1",
  "cid": "QmV1dbc4cff6db28e1eeeeb05c78c37776bb376db462",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286161,
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
      "evaluated_at": 1760286161
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
  "sig": "84987faace0aa99990bb5ba641e1941d751389c67d464ed1ac7fbea219807623"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240022849
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285765, 'matching_hash': 'fbe681be7d902297'}}}