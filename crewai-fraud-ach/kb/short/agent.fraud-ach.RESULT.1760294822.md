```json
{
  "id": "57f29466b849e3bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294822,
  "host_pid": "9e6742732c60:1",
  "hash": "55eef5d1442e4d7592a4c478ba710a8fdfd9f200114ca6ccda2ca999d4f14d8b",
  "cid": "QmV155eef5d1442e4d7592a4c478ba710a8fdfd9f200",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294822,
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
      "evaluated_at": 1760294822
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "f0ddd2a9c7cd9d9489fe8df2e0dc27d256249c0436961dd49fa3657763f75cf3"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 063100277954424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 245000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '38dcdd2f540d89c1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}