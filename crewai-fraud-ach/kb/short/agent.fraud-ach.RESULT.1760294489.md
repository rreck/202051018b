```json
{
  "id": "e0b13fa6d0e993ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294489,
  "host_pid": "9e6742732c60:1",
  "hash": "be500a344070bb1948c5ffe30286f63416919d0bc3d569106962af59f6eab6ff",
  "cid": "QmV1be500a344070bb1948c5ffe30286f63416919d0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294489,
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
      "evaluated_at": 1760294490
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
  "sig": "60de5e831478dc14f8281f6a264de82365dabdbd062ce7a0094abf779e1357c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592648645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 90391473, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'd7971b176fb0516b'}}}