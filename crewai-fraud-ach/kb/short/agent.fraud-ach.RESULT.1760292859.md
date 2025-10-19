```json
{
  "id": "595f7c15c957baa2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292859,
  "host_pid": "9e6742732c60:1",
  "hash": "53d33068269de3c3219dfa92284be41a1fe6ebc0b7499adf2c84af2278bb4756",
  "cid": "QmV153d33068269de3c3219dfa92284be41a1fe6ebc0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292859,
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
      "evaluated_at": 1760292859
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
  "sig": "8449f8e819cac18836c75ba7d4221f7e30f8eb4f14b9428587f3a70b35aa90cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 64385506, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}