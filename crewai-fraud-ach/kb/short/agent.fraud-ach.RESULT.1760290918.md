```json
{
  "id": "9a04e2b58c6325f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290918,
  "host_pid": "9e6742732c60:1",
  "hash": "c4d754994fe2e28d6df8dc2b3bd058a6191b4279f3b7aee25053df52efd8c6a5",
  "cid": "QmV1c4d754994fe2e28d6df8dc2b3bd058a6191b4279",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290918,
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
      "evaluated_at": 1760290918
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
  "sig": "b9a84fc822ab59fd2165095256fb354b5f2de48a4931ae494ebce8255a3e1208"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158642736
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 29668680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285765, 'matching_hash': '1f64147e0a165b3c'}}}