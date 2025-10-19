```json
{
  "id": "1f7147a0966551c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294231,
  "host_pid": "9e6742732c60:1",
  "hash": "7b3b6358eeab3403bfdcb3d2aed9bb7a8d02d40a25fbe950113ebed9f822d517",
  "cid": "QmV17b3b6358eeab3403bfdcb3d2aed9bb7a8d02d40a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294231,
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
      "evaluated_at": 1760294231
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
  "sig": "785fea13bffe85a89cc070e6b60dfdbfd41d34a8889dbb79c2280c711f732a1a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151593614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 96906888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '43945ca7b36522b2'}}}}