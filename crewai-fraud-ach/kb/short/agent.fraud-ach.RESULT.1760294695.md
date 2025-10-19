```json
{
  "id": "02c300be4d04898a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294695,
  "host_pid": "9e6742732c60:1",
  "hash": "a955beb2e1d85efe143fdc1749bfd7198cac49e3ddadf333f95b0704ccb4841f",
  "cid": "QmV1a955beb2e1d85efe143fdc1749bfd7198cac49e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294695,
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
      "evaluated_at": 1760294695
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
  "sig": "a90d8fdb93d387679481f94254c277ba799fcc9c8bfe209d80e56d8a88447f1b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154236496
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 88003422, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '2022d9adcee53cdf'}}}