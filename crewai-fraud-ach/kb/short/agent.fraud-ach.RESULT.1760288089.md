```json
{
  "id": "90f521faff3e22b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288089,
  "host_pid": "9e6742732c60:1",
  "hash": "e48678a0a4788033dcf77d8d5894cb131893b6c619a713ef2720ba037facef30",
  "cid": "QmV1e48678a0a4788033dcf77d8d5894cb131893b6c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288089,
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
      "evaluated_at": 1760288089
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
  "sig": "4469182ea3eaafce7cff49716cbf0c5c10c7f53ac4d9540cc9aa00cc30487e4d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 35336014, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}