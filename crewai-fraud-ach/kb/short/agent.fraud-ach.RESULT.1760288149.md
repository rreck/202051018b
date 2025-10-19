```json
{
  "id": "c2aecc83e661255d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288149,
  "host_pid": "9e6742732c60:1",
  "hash": "ab9558d3a5d0ef9a8c415607d250eb93b3a4807b42d3b59e872383e9ba48a88e",
  "cid": "QmV1ab9558d3a5d0ef9a8c415607d250eb93b3a4807b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288149,
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
      "evaluated_at": 1760288149
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
  "sig": "a9b737c9c281b170d5915907201403e793fd3d82609c57fc57e420eca5ea1c0e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271648434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 19883052, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285763, 'matching_hash': '7a167e1c4ddc5d6e'}}}