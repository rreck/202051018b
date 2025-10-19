```json
{
  "id": "219fb89c159009ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293334,
  "host_pid": "9e6742732c60:1",
  "hash": "096d1ed1174ec1269ae8a1d34a6f4ea77513ed13764f20bac0968fdbc1e60484",
  "cid": "QmV1096d1ed1174ec1269ae8a1d34a6f4ea77513ed13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293334,
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
      "evaluated_at": 1760293334
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
  "sig": "7c174b6e9d3d6c5983ea3fb27c5d81ee0392d17ea20e432ab7ef975f79c4f72d"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100279293429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 1131681888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': 'f44f07036b33cc03'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5239268}}}