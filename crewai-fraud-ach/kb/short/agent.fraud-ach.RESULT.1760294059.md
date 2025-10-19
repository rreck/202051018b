```json
{
  "id": "0c40e01f20513c0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294059,
  "host_pid": "9e6742732c60:1",
  "hash": "f776429c75ee5c38ae0ad6b7d76e7a6e1126cb6ba2553ff734b2d644205f2852",
  "cid": "QmV1f776429c75ee5c38ae0ad6b7d76e7a6e1126cb6b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294059,
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
      "evaluated_at": 1760294059
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
  "sig": "fe4ed6ebf7e571e804d83d384f3f18cf019c0b3a40e537c057a83b3afd29aa8e"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 111000024041930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 1701506730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': 'd0d1b4b42d54423e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.78, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7365830}}}