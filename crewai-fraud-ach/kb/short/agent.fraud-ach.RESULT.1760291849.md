```json
{
  "id": "8d527cc7ced74e4d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291849,
  "host_pid": "9e6742732c60:1",
  "hash": "243b832d90aa60f6b5f5e11d0c91a1320f0dfe58e60327b0d57deae38bfc243e",
  "cid": "QmV1243b832d90aa60f6b5f5e11d0c91a1320f0dfe58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291849,
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
      "evaluated_at": 1760291849
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
  "sig": "45d82ebf46ef42cb5d509881010fbf1a38ef59d2c81a09bd9c45fa38fb6e015b"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 184000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}