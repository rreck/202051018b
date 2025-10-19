```json
{
  "id": "55d8024d979c3e33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286398,
  "host_pid": "9e6742732c60:1",
  "hash": "94a47bee2529b695932c555105105bdaffc9eb5d585d6d31ccb1145d6cb87555",
  "cid": "QmV194a47bee2529b695932c555105105bdaffc9eb5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286398,
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
      "evaluated_at": 1760286398
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
  "sig": "e4263c3fe11f06f08ab766e0787bc61f677d217252bc8bf19d241e171a24c99d"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 026009594219462
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 122526384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': '4d9d7d0d036b9510'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5105266}}}