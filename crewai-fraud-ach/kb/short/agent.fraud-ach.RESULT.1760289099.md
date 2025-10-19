```json
{
  "id": "5c8eb8b2e9559353",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289099,
  "host_pid": "9e6742732c60:1",
  "hash": "f85b46fb2624616efa0a07b58b96b9906b2dd5d8379e7e03d659678affef8345",
  "cid": "QmV1f85b46fb2624616efa0a07b58b96b9906b2dd5d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289099,
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
      "evaluated_at": 1760289099
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
  "sig": "34ff5f8cc4e1712e60589e5e49e56dee30a10f26db4e6812849fb6c773681280"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022109746
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 13619777, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285765, 'matching_hash': '2a578690bb80e431'}}}