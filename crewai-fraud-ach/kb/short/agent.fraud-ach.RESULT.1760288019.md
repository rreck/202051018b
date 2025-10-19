```json
{
  "id": "ac0c35fe89a8793f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288019,
  "host_pid": "9e6742732c60:1",
  "hash": "e222a03e15089a6d4a484725c8f2528c2e0a433a06f1130446de9e80c67f83ec",
  "cid": "QmV1e222a03e15089a6d4a484725c8f2528c2e0a433a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288019,
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
      "evaluated_at": 1760288019
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
  "sig": "3d11606c5c3837a487616285b75e0f76b19b58dd93c50ee1ebaf6b6b5d327c99"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024843981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 11799360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285764, 'matching_hash': 'a5434e6981d8724b'}}}aly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.64, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9546317}}}