```json
{
  "id": "ac444eadf7ac36ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293223,
  "host_pid": "9e6742732c60:1",
  "hash": "a74ab3440018a8e94bce3fe93d54bd349972750b854f90ce2a3493d7701fcae3",
  "cid": "QmV1a74ab3440018a8e94bce3fe93d54bd349972750b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293223,
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
      "evaluated_at": 1760293223
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
  "sig": "f41396e9d18427cefd019a8d970d32ddd40fa39466772d3f001e956e0fbed47f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590136300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 106021378, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285764, 'matching_hash': '2d6fc2065b3c1287'}}}aly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.39, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8435125}}}