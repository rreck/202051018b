```json
{
  "id": "92d32c696538445f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289319,
  "host_pid": "9e6742732c60:1",
  "hash": "a62a6354e1a3221177c4e44a6de1fc0aae0e5dcc5773e750aedd99b80034be7e",
  "cid": "QmV1a62a6354e1a3221177c4e44a6de1fc0aae0e5dcc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289319,
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
      "evaluated_at": 1760289319
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
  "sig": "ebde19d70a0ff5b6ccd4b210e501803b4e4bc5ef8b914469a769ff72240ec45c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035430614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 34982160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285763, 'matching_hash': '12aaf4f6bb764c37'}}}