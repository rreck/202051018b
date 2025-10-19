```json
{
  "id": "ecb54e121d7112eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294188,
  "host_pid": "9e6742732c60:1",
  "hash": "f066efe4bd55cbbf80dd58a05f807af8234b194b2c6e616a951862f53391fd28",
  "cid": "QmV1f066efe4bd55cbbf80dd58a05f807af8234b194b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294188,
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
      "evaluated_at": 1760294188
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
  "sig": "efc5606808fb87e0214f7285fa5e16e2c65e9e9c194b0c910092a12c60e1048b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594714846
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 309, 'threshold': 50, 'total_amount': 153278214, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 308, 'first_seen': 1760284979, 'matching_hash': 'bc3982de93079c96'}}}aly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.16, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6276049}}}