```json
{
  "id": "6ebce5e694b5b4f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293292,
  "host_pid": "9e6742732c60:1",
  "hash": "b4a25b42e7c649e7a28bb68ca4c376d333d30f03d461d9175b3a7cf52d7e2b69",
  "cid": "QmV1b4a25b42e7c649e7a28bb68ca4c376d333d30f03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293292,
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
      "evaluated_at": 1760293292
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
  "sig": "123ba91a5599aa543546ab6ebb243e20d73e658c8b1c1265c7e408c441778924"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242521033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 14303735, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}