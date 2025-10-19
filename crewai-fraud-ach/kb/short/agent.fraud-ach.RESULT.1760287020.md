```json
{
  "id": "fd986a5bda77d59b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287020,
  "host_pid": "9e6742732c60:1",
  "hash": "c5c2a996a7e2d7158585a9c6a1441ce7e75dbc2a4dcc4fae97e98dc4b7ce7211",
  "cid": "QmV1c5c2a996a7e2d7158585a9c6a1441ce7e75dbc2a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287020,
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
      "evaluated_at": 1760287020
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
  "sig": "0e6e6003f9d12079dd796e71041c72f014d1e82709e41925a6fe09bff4c49a23"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 121000242247066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 408904200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285765, 'matching_hash': '1251c161514af894'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 74, 'details': {'zscore': 3.43, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9086760}}}