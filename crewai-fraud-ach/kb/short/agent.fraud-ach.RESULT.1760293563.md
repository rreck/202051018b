```json
{
  "id": "88bc4932a557d0d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293563,
  "host_pid": "9e6742732c60:1",
  "hash": "a6eec7182194ee6d1c3c102f31b490d5e3f62c4cb28ed5fd69c90d1350b2f8cd",
  "cid": "QmV1a6eec7182194ee6d1c3c102f31b490d5e3f62c4c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293563,
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
      "evaluated_at": 1760293563
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
  "sig": "aa26d0b787396e2d391ca618adaa1f156034a94c3d1ab47bb8b9eff329b5df3b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240515775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 52701207, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'c332d96fce6ec0fa'}}}maly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.93, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9380590}}}