```json
{
  "id": "2e066faea105d321",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293699,
  "host_pid": "9e6742732c60:1",
  "hash": "a373a64f55297f96407f7bba79784921eeb14cf9699cb0ea9e645f2251fa2b09",
  "cid": "QmV1a373a64f55297f96407f7bba79784921eeb14cf9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293699,
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
      "evaluated_at": 1760293699
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
  "sig": "a1c6421062df8f48109999e5043b69b8362272ae76c8b91973aa740b732d4612"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275498951
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 42600992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'a1e1622f9da312c5'}}}