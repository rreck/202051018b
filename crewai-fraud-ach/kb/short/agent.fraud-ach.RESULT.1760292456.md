```json
{
  "id": "52db62e0803d9d0a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292456,
  "host_pid": "9e6742732c60:1",
  "hash": "0420ce687addff48df1d6991b267b484c38c7295f6cff752e8efa1f17d4dbc36",
  "cid": "QmV10420ce687addff48df1d6991b267b484c38c7295",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292456,
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
      "evaluated_at": 1760292456
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
  "sig": "30bc1e3cc68b4c461e34ce28662d3f54d58539fac3657ea9d0cd05584ba551d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247026993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 87166134, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285764, 'matching_hash': '7c7d13001f766fd7'}}}