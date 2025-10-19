```json
{
  "id": "8f8cf768cc4aacab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286276,
  "host_pid": "9e6742732c60:1",
  "hash": "5e7a266400d314eb43d88c61407bca3af87d5b344fff35006d4c3f274c7aa786",
  "cid": "QmV15e7a266400d314eb43d88c61407bca3af87d5b34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286276,
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
      "evaluated_at": 1760286276
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
  "sig": "341a09d30b9c41da109e45a875b210730e57ba2a05d0fe5fabe18e892dd40edd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272135261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 30657024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760284979, 'matching_hash': 'c71937e0bf846771'}}}, 'details': {'zscore': 3.83, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9966572}}}