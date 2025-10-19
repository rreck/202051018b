```json
{
  "id": "8a84326083f6bd05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294484,
  "host_pid": "9e6742732c60:1",
  "hash": "5432a702100f6f8a3b748ba36c7819b11602712962b0f974ab825b1ba6e17288",
  "cid": "QmV15432a702100f6f8a3b748ba36c7819b116027129",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294484,
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
      "evaluated_at": 1760294484
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
  "sig": "a89b7482c62016a2e1199cf8150aec4bd852db98e8df81c754b4517c56bfa62e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151297418
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 104293147, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '6f92d94cce52eccd'}}}