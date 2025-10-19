```json
{
  "id": "2064338166c518a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290675,
  "host_pid": "9e6742732c60:1",
  "hash": "0d8dc617f8d5dede8b62be9d00222f457ee28708cefb7b130afa6fd0b681da33",
  "cid": "QmV10d8dc617f8d5dede8b62be9d00222f457ee28708",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290675,
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
      "evaluated_at": 1760290675
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
  "sig": "03d1f01734367c206a14cbfe37f2ffc8d98196a13657d8968dcdbcade00405ed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243684464
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 28123212, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285765, 'matching_hash': '4ae1f96c7cecc03b'}}}