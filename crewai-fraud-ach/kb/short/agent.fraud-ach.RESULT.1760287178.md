```json
{
  "id": "1557ab30a2786759",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287178,
  "host_pid": "9e6742732c60:1",
  "hash": "5cff5b0eacab653e1d974aa96856f85e48f5eb6d1bbea93c1116e4f40eb8c0ab",
  "cid": "QmV15cff5b0eacab653e1d974aa96856f85e48f5eb6d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287178,
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
      "evaluated_at": 1760287178
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "6e55b9fd54e0f280ad44f7c107aaeadf4fdee9f77345fb99f3130b7da000ab4f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000030152104
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 14836257, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285763, 'matching_hash': 'f9baa0480a932ad2'}}}