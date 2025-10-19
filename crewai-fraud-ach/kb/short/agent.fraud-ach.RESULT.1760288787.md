```json
{
  "id": "8aca4f90aba28e35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288787,
  "host_pid": "9e6742732c60:1",
  "hash": "e67bc97840d96c0a234d1400a81d4abd6cbb8bec3590d64f03a137d69e0eff4d",
  "cid": "QmV1e67bc97840d96c0a234d1400a81d4abd6cbb8bec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288787,
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
      "evaluated_at": 1760288787
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
  "sig": "f95aafc8d0c169b0c09b2f308c7d9d5c2fc89f1f9fb856142b4634e75b56149c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243431079
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 13504192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285764, 'matching_hash': '441814efc7e72dab'}}}