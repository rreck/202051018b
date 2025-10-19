```json
{
  "id": "8725e3bcb9c4a185",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292527,
  "host_pid": "9e6742732c60:1",
  "hash": "683dc41639000a1c6ba109ec1a93e01108a85e258246bc9da35fecbb19487ec0",
  "cid": "QmV1683dc41639000a1c6ba109ec1a93e01108a85e25",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292527,
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
      "evaluated_at": 1760292527
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
  "sig": "b5523946a2c5b3d98e628c6b787c436cc607bd9b751b14a003c71afea993a830"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 199000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}