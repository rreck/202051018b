```json
{
  "id": "d7500b2a2f21bb18",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294327,
  "host_pid": "9e6742732c60:1",
  "hash": "cada435315d79c8b2eab51c1f7de62f843e0849ef915cb5f1c4ffe20a8dc478e",
  "cid": "QmV1cada435315d79c8b2eab51c1f7de62f843e0849e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294327,
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
      "evaluated_at": 1760294327
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
  "sig": "721f27fc9808bb62b4e14f4b7e71ffe363aa6ec291a8693f29898aa779a83008"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 063100277592839
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 236000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'd907a2a28cc997b7'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}