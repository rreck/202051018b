```json
{
  "id": "1df25e40cdc031b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290042,
  "host_pid": "9e6742732c60:1",
  "hash": "3072bad97d6df40542df2c40a44d2cc51623ff6028b26501f14a9a9cf14f1f05",
  "cid": "QmV13072bad97d6df40542df2c40a44d2cc51623ff60",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290042,
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
      "evaluated_at": 1760290042
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
  "sig": "215c9a789aea044945a50b06e2705ac454248311a7f3e0e82a15f33c964a75e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242172457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 65963800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': '180325de6151a8c9'}}}