```json
{
  "id": "876918fb2d25d0fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291186,
  "host_pid": "9e6742732c60:1",
  "hash": "1af140ed217ee3b8bae93d188a3f1626d7317f52b4c632856a69f9e870fc15c1",
  "cid": "QmV11af140ed217ee3b8bae93d188a3f1626d7317f52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291186,
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
      "evaluated_at": 1760291186
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
  "sig": "590a9893a9f2cb9921bb5cefdec44d6c1aa1516993c5620033c0b4e38e3970a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153448153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 81667053, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285764, 'matching_hash': '55db9843fa0daece'}}}