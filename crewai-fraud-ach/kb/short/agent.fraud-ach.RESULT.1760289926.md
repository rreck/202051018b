```json
{
  "id": "1d8f6fa0cc9ede82",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289926,
  "host_pid": "9e6742732c60:1",
  "hash": "314f8cfbff5903d91c5d8dfd0f656ff7eb1b8acfb34a732e1731e8b2572c661f",
  "cid": "QmV1314f8cfbff5903d91c5d8dfd0f656ff7eb1b8acf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289926,
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
      "evaluated_at": 1760289926
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "2a46afc1c769dc4b7919827f29210b377f2d1ef9e19f040978a3e886b0faa395"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201467541453
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 68500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '2d82340c3dc0e840'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}