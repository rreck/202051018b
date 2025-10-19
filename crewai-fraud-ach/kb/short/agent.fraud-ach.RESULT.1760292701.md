```json
{
  "id": "6eb90985c2b000ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292701,
  "host_pid": "9e6742732c60:1",
  "hash": "d184fb9771664a6add0dfd6c058cbddb9f7ba305d1bff646a54995afbf046248",
  "cid": "QmV1d184fb9771664a6add0dfd6c058cbddb9f7ba305",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292701,
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
      "evaluated_at": 1760292701
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "6493bd386ababbb2562442db4671e760c3a5c3913a0f65706f7585924d072a83"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 044000039260642
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 279, 'threshold': 50, 'total_amount': 1561196952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 278, 'first_seen': 1760284979, 'matching_hash': 'a7542f9d69c5b02c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5595688}}}