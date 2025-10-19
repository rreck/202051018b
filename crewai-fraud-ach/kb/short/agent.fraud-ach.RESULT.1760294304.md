```json
{
  "id": "d0d3170f2790b0f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294304,
  "host_pid": "9e6742732c60:1",
  "hash": "14c1e790add1b88ef900ce6ae0b3673d1fb9348f3e9db4f668b3f43c3913adf3",
  "cid": "QmV114c1e790add1b88ef900ce6ae0b3673d1fb9348f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294304,
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
      "evaluated_at": 1760294304
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
  "sig": "fa80e9d48358590109d678e541f37fa85a89961ba0c7ad3c3e4867718e3621e7"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 121000248309566
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 235000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285765, 'matching_hash': '25ac79dd28618198'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}