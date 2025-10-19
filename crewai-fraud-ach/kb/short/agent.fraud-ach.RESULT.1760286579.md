```json
{
  "id": "2a61c4ab47f819c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286579,
  "host_pid": "9e6742732c60:1",
  "hash": "7260d66c90af64325e254d69d1755cc3c2aba426929ce27099779d6997eae857",
  "cid": "QmV17260d66c90af64325e254d69d1755cc3c2aba426",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286579,
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
      "evaluated_at": 1760286579
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
  "sig": "c35e6d0d8d217bd4649fff15cb840c9aa7e93783fe381f9094debc7d4300c220"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 026009591320033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 241565460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285764, 'matching_hash': '73d2316250f00dec'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8052182}}}