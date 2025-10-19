```json
{
  "id": "9fc60190e8aec07a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291735,
  "host_pid": "9e6742732c60:1",
  "hash": "c479381b1852aafe4b4352d55d58769a7f9721a70f53d0866df4b67d6f08fab1",
  "cid": "QmV1c479381b1852aafe4b4352d55d58769a7f9721a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291735,
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
      "evaluated_at": 1760291735
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
  "sig": "bd859bfc2b722f5831484f90b2ddd05ecc9f5856ec92bd4204290bf0d194d36d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596228885
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 80415062, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '9b2dabf2ca05df4f'}}}