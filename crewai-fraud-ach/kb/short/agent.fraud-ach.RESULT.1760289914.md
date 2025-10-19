```json
{
  "id": "bdc99c803677e9e7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289914,
  "host_pid": "9e6742732c60:1",
  "hash": "a0a4cfe7b8068c01b86483b0fed791ec7cbfa8c02d312b001630f92ba199cd4b",
  "cid": "QmV1a0a4cfe7b8068c01b86483b0fed791ec7cbfa8c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289914,
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
      "evaluated_at": 1760289914
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
  "sig": "a77f44d5c816da8ad841e629ced4bbcc0f14784feb47b08024bd2a6fe9efd720"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 136000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}