```json
{
  "id": "3e31ef3dad0444f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291626,
  "host_pid": "9e6742732c60:1",
  "hash": "21ce1fe125c5fcf4e96f93b90f451ae8a9c9d0b616a1f1a287eb914a597cae08",
  "cid": "QmV121ce1fe125c5fcf4e96f93b90f451ae8a9c9d0b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291626,
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
      "evaluated_at": 1760291626
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
  "sig": "f14c874d9d4ac11c3b9b9f1d4a3c3cf5b8550708f69206fb1e626cb4e138c584"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031910208
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 68235158, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': '8397d9ba38a9dfb7'}}}