```json
{
  "id": "12d9f475f2f33a2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291066,
  "host_pid": "9e6742732c60:1",
  "hash": "0ac563c2f32c259a0fccf074e5c1b39737257c30631fd1f126db89255e601eb9",
  "cid": "QmV10ac563c2f32c259a0fccf074e5c1b39737257c30",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291066,
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
      "evaluated_at": 1760291066
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
  "sig": "46c20402454dd974b9c14057336e932e856c1cbbb224d926a38d4df7b7c384b9"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 063100273353772
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 166000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285764, 'matching_hash': '39c5bac7d3007e29'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}