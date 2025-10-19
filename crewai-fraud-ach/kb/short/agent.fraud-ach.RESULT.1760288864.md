```json
{
  "id": "14771142c7a4d72f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288864,
  "host_pid": "9e6742732c60:1",
  "hash": "b71be315e54fcd95a5984f65289958b15f236fe683bb399659c96c52f21dbec6",
  "cid": "QmV1b71be315e54fcd95a5984f65289958b15f236fe6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288864,
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
      "evaluated_at": 1760288864
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
  "sig": "a90b99693adcfd54ee172a1a4c9901a47b662676df4ca69ca11f5483d46cf6a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 22636618, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285764, 'matching_hash': 'bf601f225a65579b'}}}