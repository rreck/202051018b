```json
{
  "id": "f1fdcc8678c7059a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294778,
  "host_pid": "9e6742732c60:1",
  "hash": "a9a4c6f2421e237209f0b9d01ad48768abd85b807c004142a8625f637883e81d",
  "cid": "QmV1a9a4c6f2421e237209f0b9d01ad48768abd85b80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294778,
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
      "evaluated_at": 1760294778
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
  "sig": "27fa072745cbd62798ca4cd091971f5fbb4e6ab05cf611c19f5d64408c8a32e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249127775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 35097936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '35c1bd481e0f1f5f'}}}