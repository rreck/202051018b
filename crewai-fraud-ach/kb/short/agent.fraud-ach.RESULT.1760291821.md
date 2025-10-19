```json
{
  "id": "2baef7c2e85928f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291821,
  "host_pid": "9e6742732c60:1",
  "hash": "4b23ebe143b84a51fa294e08878186a31c26db5432ef74341d61cd5a0e4a1481",
  "cid": "QmV14b23ebe143b84a51fa294e08878186a31c26db54",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291821,
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
      "evaluated_at": 1760291821
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
  "sig": "a603b677dd4a656078959b7e868c5a7802514c3d7427978e7631099631ecf9b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038087823
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 77358936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '9ca4fa9f5ff6e727'}}}