```json
{
  "id": "ecba4dfe68af08e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291476,
  "host_pid": "9e6742732c60:1",
  "hash": "d4daf99b02438291fdb500b625adc1ae9f2e4b61e298a40d133e301eee4a61ef",
  "cid": "QmV1d4daf99b02438291fdb500b625adc1ae9f2e4b61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291476,
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
      "evaluated_at": 1760291476
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
  "sig": "151c697acdd652013ec6eb2d0498ac8f90fed8980d29e6757ca8a6978a5e058a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469028209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 42968464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': 'a4269a968e85dafe'}}}