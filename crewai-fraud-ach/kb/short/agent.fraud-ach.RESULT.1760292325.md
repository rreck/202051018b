```json
{
  "id": "a872597fa1ec4042",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292325,
  "host_pid": "9e6742732c60:1",
  "hash": "042cfb721699fb533c4a6061585ae628cc8570aa0da8ba3e3b1a79d81f2523c9",
  "cid": "QmV1042cfb721699fb533c4a6061585ae628cc8570aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292325,
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
      "evaluated_at": 1760292325
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
  "sig": "1a82ba4aaa790ba7efe1b0e86af9da7bc2d88af59c5a8cc5645129e67aea0d34"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592426992
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 83221515, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '6c96fa15a49bffda'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}