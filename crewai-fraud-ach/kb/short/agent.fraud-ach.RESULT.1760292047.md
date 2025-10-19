```json
{
  "id": "f2539da9fec1ffc4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292047,
  "host_pid": "9e6742732c60:1",
  "hash": "c1e3cc16bad709b93404f8997a5024a6adf183cc0522f317a11499f08d1d6724",
  "cid": "QmV1c1e3cc16bad709b93404f8997a5024a6adf183cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292047,
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
      "evaluated_at": 1760292047
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "2e834e57b179e4d9d6a9a23ca7cfe3639116dab0f06e16b6c54820c320b49b66"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154361187
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 47250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285764, 'matching_hash': 'a57b8c5e7960514a'}}}maly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.3, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6511445}}}