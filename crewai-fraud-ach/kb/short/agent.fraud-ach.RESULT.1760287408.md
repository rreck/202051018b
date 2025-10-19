```json
{
  "id": "5677d3604d66988a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287408,
  "host_pid": "9e6742732c60:1",
  "hash": "09ebce5f4ba71dc5cca6cd3c56b3cce061099efdc37ed0c00156c6bc288c2e73",
  "cid": "QmV109ebce5f4ba71dc5cca6cd3c56b3cce061099efd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287408,
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
      "evaluated_at": 1760287408
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
  "sig": "96c4b32a8cfb4b7964bdcc00b1b294d1f5d60c795894b26f70bff28a02f4ae9a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105154224764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 14247615, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285763, 'matching_hash': '73218c90107a537b'}}}