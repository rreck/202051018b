```json
{
  "id": "755966cb60557dbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290873,
  "host_pid": "9e6742732c60:1",
  "hash": "6968f7c9d77a42eeb28fe8cceb7fe33fbcd43fdbd1bc4f98d36b3411a0d46c46",
  "cid": "QmV16968f7c9d77a42eeb28fe8cceb7fe33fbcd43fdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290873,
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
      "evaluated_at": 1760290873
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
  "sig": "3396199a289ed74df07a842e2fb1562e43bd265767b7fa84b8d16b185c07fb54"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032369849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 67213636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285764, 'matching_hash': '11b86d7f8733bf3d'}}}