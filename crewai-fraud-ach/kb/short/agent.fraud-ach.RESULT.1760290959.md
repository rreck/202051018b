```json
{
  "id": "a978c906ac8a358f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290959,
  "host_pid": "9e6742732c60:1",
  "hash": "fb2f21080c22bcc9254f668665c5c8f546f9ae3f59fa7fc421b81b7ff399a7be",
  "cid": "QmV1fb2f21080c22bcc9254f668665c5c8f546f9ae3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290959,
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
      "evaluated_at": 1760290959
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
  "sig": "a6330c7c7aba4777b4b9ba69690e72c50163165103b56e48037eea43d7b71bd8"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 163000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}