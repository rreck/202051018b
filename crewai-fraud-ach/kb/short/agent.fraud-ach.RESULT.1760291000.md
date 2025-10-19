```json
{
  "id": "642550b7bf3340c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291000,
  "host_pid": "9e6742732c60:1",
  "hash": "4eacf66a1c0aad4b42996bccb8c96af9b530393b3f3b84d10b0e41475d10250e",
  "cid": "QmV14eacf66a1c0aad4b42996bccb8c96af9b530393b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291000,
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
      "evaluated_at": 1760291000
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
  "sig": "b3336424e96f5ec9b652e3f3bffc773a05d6b627b0a602e1cd49174e1f062f05"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462408143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 79742212, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285765, 'matching_hash': '36407d3e627869a5'}}}