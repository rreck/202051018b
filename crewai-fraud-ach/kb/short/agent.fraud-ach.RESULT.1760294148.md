```json
{
  "id": "a8353cb936d772f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294148,
  "host_pid": "9e6742732c60:1",
  "hash": "71c39e5c7ee5ade73315839139decc38fbfbe3810610207f37250fa5bd434c14",
  "cid": "QmV171c39e5c7ee5ade73315839139decc38fbfbe381",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294148,
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
      "evaluated_at": 1760294148
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
  "sig": "8afaef4fb005c82a599a7b80ecbdcbc21602abffa470e0001a050b6d613e7d55"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273742232
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 48911864, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': '98264f1e6b5ab805'}}}