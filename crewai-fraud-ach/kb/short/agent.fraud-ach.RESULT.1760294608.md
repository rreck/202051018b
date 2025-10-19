```json
{
  "id": "c1a9fca0ef8514a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294608,
  "host_pid": "9e6742732c60:1",
  "hash": "35cab45fe6d1d2196a8593fccdde8cea9e0134f28e57b12031252d03ce54980a",
  "cid": "QmV135cab45fe6d1d2196a8593fccdde8cea9e0134f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294608,
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
      "evaluated_at": 1760294608
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
  "sig": "70730bf355693388fa3346ae8801491dda36f3cfda50d3a33f13a2065eb1d603"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039536800
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 43062362, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '37ca22243c3304cf'}}}