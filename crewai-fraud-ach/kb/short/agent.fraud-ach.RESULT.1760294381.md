```json
{
  "id": "2c5535a02a14e629",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294381,
  "host_pid": "9e6742732c60:1",
  "hash": "d7ee40402cf9d63a79153ec846e6efcbb22aa181c65caa845bee51a107596d69",
  "cid": "QmV1d7ee40402cf9d63a79153ec846e6efcbb22aa181",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294381,
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
      "evaluated_at": 1760294381
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
  "sig": "82af1c2eae8136f27cddccd0718fa2f128915f0fadd2ec30d5abcbee884e2896"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 063100277592839
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 237000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'd907a2a28cc997b7'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}