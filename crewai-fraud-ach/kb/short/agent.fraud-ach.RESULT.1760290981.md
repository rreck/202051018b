```json
{
  "id": "26d605081ccca0d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290981,
  "host_pid": "9e6742732c60:1",
  "hash": "68aa03c249213c16d9eea2719ab784a55c4b537ab714bedeb697660b0c6846a0",
  "cid": "QmV168aa03c249213c16d9eea2719ab784a55c4b537a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290981,
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
      "evaluated_at": 1760290981
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
  "sig": "ccb0652d3aa8c91e69a13d90ba5ceca7375e48e088896fee20b09aa460a0c3fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248879476
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 31200836, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '88da1f364f410d45'}}}maly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.35, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6602570}}}