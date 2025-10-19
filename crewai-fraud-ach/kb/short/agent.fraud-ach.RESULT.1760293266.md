```json
{
  "id": "c14ec248173a13a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293266,
  "host_pid": "9e6742732c60:1",
  "hash": "abbefa0846992aa026c950a50b582f4fbb3c2d0594880946ba7a686c162cbe33",
  "cid": "QmV1abbefa0846992aa026c950a50b582f4fbb3c2d05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293266,
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
      "evaluated_at": 1760293266
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
  "sig": "13bbc3982f8b278cd51ff5331b6cdbb67ec290377d1a2966b5bb694e002dc6c4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034782199
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 23381895, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '89ad1f50f76a063c'}}}