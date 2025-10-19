```json
{
  "id": "1cd7a7b5fd4a1beb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292894,
  "host_pid": "9e6742732c60:1",
  "hash": "a28c4002a08c025bd5ac4f8dd4487041154b36c55b202edc81bda5926449028b",
  "cid": "QmV1a28c4002a08c025bd5ac4f8dd4487041154b36c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292894,
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
      "evaluated_at": 1760292894
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
  "sig": "ed5fc418723638fd2911f3c624ab413976b9e61805fba93acf08f6709bab1169"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026697062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 283, 'threshold': 50, 'total_amount': 90355674, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 282, 'first_seen': 1760284979, 'matching_hash': 'f9d80f2e7cffa5ec'}}}maly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.16, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6276049}}}