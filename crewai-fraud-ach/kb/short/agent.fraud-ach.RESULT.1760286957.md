```json
{
  "id": "8628bb119cd1e630",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286957,
  "host_pid": "9e6742732c60:1",
  "hash": "ce81e08a01e61b2da15bc7433f58b369048e04bdf40d74149ea938036aca4817",
  "cid": "QmV1ce81e08a01e61b2da15bc7433f58b369048e04bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286957,
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
      "evaluated_at": 1760286957
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "fc44f94e26bc3fe05582436a51afae6de9ffd39d5d64d7a4324e4bf92e8f0bbe"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000030595065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13066453, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285763, 'matching_hash': '3889a0f66c8870f8'}}}