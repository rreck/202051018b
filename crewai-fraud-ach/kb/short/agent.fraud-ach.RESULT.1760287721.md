```json
{
  "id": "fb66f31252b3ddde",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287721,
  "host_pid": "9e6742732c60:1",
  "hash": "1359f3dc558a31f3f493aeb02cee6a6b6236b209f94de10735eb8d6460d37512",
  "cid": "QmV11359f3dc558a31f3f493aeb02cee6a6b6236b209",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287721,
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
      "evaluated_at": 1760287721
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
  "sig": "73bb2a3d5879093bed7b132ea532f2f93491d35a79e0cc2b178a0c312bd1c17d"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 122105153734827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 34541150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285764, 'matching_hash': 'f575a9f929aab221'}}}