```json
{
  "id": "dafa7e7a52ee09eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289133,
  "host_pid": "9e6742732c60:1",
  "hash": "248d08aeb5131d1b4fedcb1bfb42c913ac515fea18b5e7dd9c47279c9838de16",
  "cid": "QmV1248d08aeb5131d1b4fedcb1bfb42c913ac515fea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289133,
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
      "evaluated_at": 1760289133
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
  "sig": "a0a05aa2bece1276ba15623d04df681386d330a0f065a8fd2c94ddd025e2ed41"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 37422324, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}