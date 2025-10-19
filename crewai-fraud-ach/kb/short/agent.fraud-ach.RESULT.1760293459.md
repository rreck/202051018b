```json
{
  "id": "bff86945209db679",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293459,
  "host_pid": "9e6742732c60:1",
  "hash": "83b56aee0676c6e10ccf6c47db38270c194f1337ad0dbfdf39a29bd9adf27f57",
  "cid": "QmV183b56aee0676c6e10ccf6c47db38270c194f1337",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293459,
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
      "evaluated_at": 1760293459
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
  "sig": "818310a51289f233e82b7b13e6ccb8b60ff888a04e0a89c0fa51f3d5abb680f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029122182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 21900000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': '6eeeaf20a2fbd10d'}}}