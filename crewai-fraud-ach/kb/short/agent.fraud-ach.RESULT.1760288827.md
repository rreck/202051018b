```json
{
  "id": "011e34a9e89ac591",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288827,
  "host_pid": "9e6742732c60:1",
  "hash": "9c54904726f716fb92b811581bfb34cb15cc4217109b5e7ccd0cf64d72092470",
  "cid": "QmV19c54904726f716fb92b811581bfb34cb15cc4217",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288827,
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
      "evaluated_at": 1760288827
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
  "sig": "e7ff89e7a4ef2dea0da73e47f8c9d17a566cb11df2ac0d5bb1e9e036d151cc07"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029163318
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 32387985, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285765, 'matching_hash': 'b5567c8565e47211'}}}