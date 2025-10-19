```json
{
  "id": "fd73f48931de644b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289870,
  "host_pid": "9e6742732c60:1",
  "hash": "2578e07a9b2b1a727cdf3b2df76e11a8ed95d435a8d20d58cadd582c661418d7",
  "cid": "QmV12578e07a9b2b1a727cdf3b2df76e11a8ed95d435",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289870,
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
      "evaluated_at": 1760289870
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
  "sig": "f38c831d686b2fe8c4ccab8d6b1cb6f66164aa59615343d35c1457e2ff8cd99d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594711181
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 19712700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285765, 'matching_hash': '37ffc636e48dfc6b'}}}