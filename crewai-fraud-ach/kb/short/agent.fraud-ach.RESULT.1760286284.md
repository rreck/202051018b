```json
{
  "id": "f47cc4f1ab3cf28f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286284,
  "host_pid": "9e6742732c60:1",
  "hash": "a482c121cdb978c7d1b52f79ec7a798af0c58e755898ee0b0d9bca107749047f",
  "cid": "QmV1a482c121cdb978c7d1b52f79ec7a798af0c58e75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286284,
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
      "evaluated_at": 1760286284
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "e22aaf7cbdc2be964bd1e93e7e6539b492093f110c494af848cf54143592204f"
}
```

Fraud detected: amount_anomaly (score: 75)
Transaction: 121000241325245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 163193100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285765, 'matching_hash': '97920a0a35eda98b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.02, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8159655}}}