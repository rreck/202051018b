```json
{
  "id": "f2d3472ec6555db9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294186,
  "host_pid": "9e6742732c60:1",
  "hash": "fb46b6d0b045993157a5403d1cfca6fe29bb11e4fe9a094446b82b8668c5d5d3",
  "cid": "QmV1fb46b6d0b045993157a5403d1cfca6fe29bb11e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294186,
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
      "evaluated_at": 1760294186
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
  "sig": "beef637033376114d133a78609ea29ed10e4234d35e2d28efc1978afd40afaa4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024242004
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 58250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': '99660a13145cb677'}}}