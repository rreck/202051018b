```json
{
  "id": "232143857dcc2cee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291249,
  "host_pid": "9e6742732c60:1",
  "hash": "af249d7d80f73146978b85f6c5a8c94a04b95379a2dc50a1b81310b38a47f38a",
  "cid": "QmV1af249d7d80f73146978b85f6c5a8c94a04b95379",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291249,
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
      "evaluated_at": 1760291249
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
  "sig": "aebea659d9b2700bbedf1b0e96ddb7f7317255e0bb34274dd7766676d475b435"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 170000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}