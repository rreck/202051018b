```json
{
  "id": "498a92cc1797865a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291546,
  "host_pid": "9e6742732c60:1",
  "hash": "704c62e09ae91d1f3b84477bc948761ca540bf4116c66eddf203ac1c80d16d17",
  "cid": "QmV1704c62e09ae91d1f3b84477bc948761ca540bf41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291546,
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
      "evaluated_at": 1760291546
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
  "sig": "421c468e4eda64df09f2c7170f2909da9d31008af30e8c599aa3d572cbe5ffe6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463448865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 30417981, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285765, 'matching_hash': '5a565595f8571aef'}}}