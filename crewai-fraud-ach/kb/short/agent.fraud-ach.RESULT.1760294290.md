```json
{
  "id": "bbffa4952b955ec2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294290,
  "host_pid": "9e6742732c60:1",
  "hash": "eb9f7b0384b2a5b053174501b44f3b2b526cc01f8945e2151bbb21cbe6f42187",
  "cid": "QmV1eb9f7b0384b2a5b053174501b44f3b2b526cc01f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294290,
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
      "evaluated_at": 1760294290
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
  "sig": "3c9a8bb807f075f3f4e7d4af9d3978e0dbdf80db7c349751e63c22680d4fb318"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465763935
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 93222150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '9c229bcc2f82b898'}}}