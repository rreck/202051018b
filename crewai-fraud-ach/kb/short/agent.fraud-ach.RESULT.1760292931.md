```json
{
  "id": "61f54da4217dc8ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292931,
  "host_pid": "9e6742732c60:1",
  "hash": "07c1bd1fe08f0801f7d8e79389f03e67b9d03d7b4d3062576bbef4edf2345c8b",
  "cid": "QmV107c1bd1fe08f0801f7d8e79389f03e67b9d03d7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292931,
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
      "evaluated_at": 1760292931
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
  "sig": "3bd1a6ba66bd5e82e4aba29b03b8a80638982fbb7ed7495b2dcf22641525f128"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026701294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 53591824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285764, 'matching_hash': 'c6488d75609f0f90'}}}