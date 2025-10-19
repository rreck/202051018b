```json
{
  "id": "531cf9488d4318ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293732,
  "host_pid": "9e6742732c60:1",
  "hash": "94e2f4a5c555c8d0e1b20cfdf0ca05168fe1e86360e6aa9cc34c6aff19877a06",
  "cid": "QmV194e2f4a5c555c8d0e1b20cfdf0ca05168fe1e863",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293732,
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
      "evaluated_at": 1760293732
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
  "sig": "29f0795bd30028f0c7787a97bbd31836954688323a1e954821c5e93f8e3fbff6"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 021000026547506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 224000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285764, 'matching_hash': 'e0a909ce459a76c8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}