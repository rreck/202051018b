```json
{
  "id": "58b8c2b009702f9d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292515,
  "host_pid": "9e6742732c60:1",
  "hash": "0f8491b91d31dc4d52b38e67b3dbd4093cde107a083711942e9fb93493c5e874",
  "cid": "QmV10f8491b91d31dc4d52b38e67b3dbd4093cde107a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292515,
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
      "evaluated_at": 1760292515
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
  "sig": "c12ec53d2cae1afdc7b1bc32819270a6a48acbca3a7d58a4a568a34cbda43bca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037779899
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 81794373, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285765, 'matching_hash': '90378a324202fffb'}}}