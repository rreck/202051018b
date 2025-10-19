```json
{
  "id": "93167cbdad422139",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292659,
  "host_pid": "9e6742732c60:1",
  "hash": "f5143df61805a953fc025aafd42fef986c15bbfac85302142d0075fe83e0748f",
  "cid": "QmV1f5143df61805a953fc025aafd42fef986c15bbfa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292659,
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
      "evaluated_at": 1760292659
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
  "sig": "7c8e527c5113b3e6f4b56163fa1c9d6b4af8f3d60634acb52f76665c90efdf4e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243177921
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 69623340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': '2e3fb8f97f4f3efd'}}}