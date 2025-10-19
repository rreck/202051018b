```json
{
  "id": "7bcd1711f6b49fcd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291333,
  "host_pid": "9e6742732c60:1",
  "hash": "5fa894565262a8c23bfc6c67c4c214d010fcf213dae0fe5939743d7a4c9bc4e4",
  "cid": "QmV15fa894565262a8c23bfc6c67c4c214d010fcf213",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291333,
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
      "evaluated_at": 1760291333
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
  "sig": "04848b28b3120cc6910d9387135fb5afdcb0b9d35b3e96951358f1e65c3e33cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023496704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 58317116, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285765, 'matching_hash': 'f379baac52e28232'}}}