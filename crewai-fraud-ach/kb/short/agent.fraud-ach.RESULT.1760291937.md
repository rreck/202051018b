```json
{
  "id": "309356f5b322ff34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291937,
  "host_pid": "9e6742732c60:1",
  "hash": "27e79eac218d5fa5e716b345846261fa3a58cd4d8be05ceea2ae7d12faa3d5b1",
  "cid": "QmV127e79eac218d5fa5e716b345846261fa3a58cd4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291937,
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
      "evaluated_at": 1760291937
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
  "sig": "2010fb10d7780ef7881f1d19dd5168b435b58c5f8619318fc1783718cc9fd9f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021517830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 55369038, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285765, 'matching_hash': '323b6ce2946b0561'}}}