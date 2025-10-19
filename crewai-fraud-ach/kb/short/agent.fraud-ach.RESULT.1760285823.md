```json
{
  "id": "bc1d0709157f2d7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285823,
  "host_pid": "9e6742732c60:1",
  "hash": "8c86e88149dde6cfc3d12af88348c878b071a7703fd0240270c17783419838c6",
  "cid": "QmV18c86e88149dde6cfc3d12af88348c878b071a770",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285823,
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
      "evaluated_at": 1760285823
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
  "sig": "97591e8aafce0c5c723e155ea54feae3db36cdb3ed0fc1867fc606dc448dc5a5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000024591055
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285763, 'matching_hash': '8a72f4eb6bbba5d7'}}}