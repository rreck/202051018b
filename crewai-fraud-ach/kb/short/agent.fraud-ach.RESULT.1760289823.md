```json
{
  "id": "ec81e60f1b93b4cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289823,
  "host_pid": "9e6742732c60:1",
  "hash": "7fb3ec83530433141cb5a7c207cde8238bcfa06127c7b2a7064a149080b88875",
  "cid": "QmV17fb3ec83530433141cb5a7c207cde8238bcfa061",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289823,
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
      "evaluated_at": 1760289823
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
  "sig": "0074931011c36fbc1b762089b958bdcad5c945db791eb2974f4e0460e3e2ebb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021988031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 33884178, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285764, 'matching_hash': '88465ad333807d91'}}}