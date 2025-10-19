```json
{
  "id": "34c1b93d6ff39d99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291959,
  "host_pid": "9e6742732c60:1",
  "hash": "9404c592e32c29a2481d061033948d93ca1ff58b455a68705ac6f558aabaf23e",
  "cid": "QmV19404c592e32c29a2481d061033948d93ca1ff58b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291959,
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
      "evaluated_at": 1760291959
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
  "sig": "5cd19c43cb6f213aa4cd80ab2071bb635c04c376d5799910dbbb1c70029d4bb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276330055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 84235646, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '5c86a9c2afef995d'}}}maly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9245331}}}