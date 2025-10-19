```json
{
  "id": "842e9a5741e69976",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290661,
  "host_pid": "9e6742732c60:1",
  "hash": "09ccb58bab06d490b077a6596b7da075e71c5065e28d0904dd97e400fca166be",
  "cid": "QmV109ccb58bab06d490b077a6596b7da075e71c5065",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290661,
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
      "evaluated_at": 1760290661
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
  "sig": "f0e3f837a751f5ac6100de07e9e46803b19e8758130e1e92f3aa5e35a7d60f6e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246379487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 74661132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285764, 'matching_hash': 'aafc2265b0403e69'}}}