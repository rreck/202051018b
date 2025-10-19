```json
{
  "id": "a06deed0f25a8b0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291123,
  "host_pid": "9e6742732c60:1",
  "hash": "b2629d137e3bc77654df51fa3b79c538711ceae010c71b5dc44d2035a9c6aca7",
  "cid": "QmV1b2629d137e3bc77654df51fa3b79c538711ceae0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291123,
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
      "evaluated_at": 1760291123
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
  "sig": "c799fc6bc6befb8bf817424a0c23ea7a6bfb0224d5e11780571c5b301f8a6a23"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 41750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285765, 'matching_hash': '9c2417d6ee361cba'}}}