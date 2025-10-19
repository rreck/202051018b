```json
{
  "id": "d5fac6821b5359fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293122,
  "host_pid": "9e6742732c60:1",
  "hash": "da087a1be4582e2342757ee2c87b2bc32792937a94afd990bfdae540eb8c2817",
  "cid": "QmV1da087a1be4582e2342757ee2c87b2bc32792937a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293122,
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
      "evaluated_at": 1760293122
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
  "sig": "4102d46e838086c3d59a229764832ccc1720eda0cb67a26217c21637d1aace32"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249268740
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 16448232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '2b1c4c9f55d7dd69'}}}