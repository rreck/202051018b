```json
{
  "id": "e7ff90bd0b6fd3d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287524,
  "host_pid": "9e6742732c60:1",
  "hash": "11e9d687ac7cfd06d50eaf673378905ac5cff8e3f349f39a622fa9b7b90bb3a8",
  "cid": "QmV111e9d687ac7cfd06d50eaf673378905ac5cff8e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287524,
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
      "evaluated_at": 1760287524
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
  "sig": "050506415b435cc3a3c7f1e27bea5b9fc8e73df68242fe89acdd59d6d7bb06a8"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 21486654, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}