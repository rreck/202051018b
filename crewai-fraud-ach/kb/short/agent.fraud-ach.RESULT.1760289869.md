```json
{
  "id": "2a530b000dc3442b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289869,
  "host_pid": "9e6742732c60:1",
  "hash": "d5f2971a9a134e813cfa0d1ea63e2384dc0c840be2eb939cfddd31ce2a3f900a",
  "cid": "QmV1d5f2971a9a134e813cfa0d1ea63e2384dc0c840b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289869,
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
      "evaluated_at": 1760289869
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
  "sig": "c0f07d3e7cf2781d260f00883c4257cb3d0e20b1c44e1931554164a9664db49b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279970164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 24928020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285765, 'matching_hash': 'dc8a7598801f2a18'}}}