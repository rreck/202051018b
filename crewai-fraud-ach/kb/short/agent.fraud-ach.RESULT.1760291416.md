```json
{
  "id": "a9d6391910e7692c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291416,
  "host_pid": "9e6742732c60:1",
  "hash": "0ebec64967fe0f3352be165a1fa144d8d5351a60bdf30d8f51f59d2300082e35",
  "cid": "QmV10ebec64967fe0f3352be165a1fa144d8d5351a60",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291416,
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
      "evaluated_at": 1760291416
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
  "sig": "6306bc84dd27122421697addc3559c345360d21375080aeb75a07939fa7b56c0"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 121000248309566
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 174000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285765, 'matching_hash': '25ac79dd28618198'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}