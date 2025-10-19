```json
{
  "id": "5c6c8a81cb27c847",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290898,
  "host_pid": "9e6742732c60:1",
  "hash": "520cb456f422c6043a6bfcd75968e7d8ce75b19a02dee7a62a5a9df8af2b43b8",
  "cid": "QmV1520cb456f422c6043a6bfcd75968e7d8ce75b19a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290898,
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
      "evaluated_at": 1760290898
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
  "sig": "279cbfa0905de9c5338b4de292fb4ee8c487af8d01038f9730e4846e21fcf6f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027747327
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 52869996, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': 'bf09531d82abcda7'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '542300570', 'validation_error': 'Invalid routing number checksum'}}}