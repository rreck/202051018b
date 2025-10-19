```json
{
  "id": "2eeeeb7bbba94c3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288952,
  "host_pid": "9e6742732c60:1",
  "hash": "81ed689ab0b5fe62a9da8e3c0670059241a73fb77699f4e7c3695565da4ba84f",
  "cid": "QmV181ed689ab0b5fe62a9da8e3c0670059241a73fb7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288952,
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
      "evaluated_at": 1760288952
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
  "sig": "ce580c7571ae453e167c7a49cb10e4946f7c24d533f747fad66d59ac3f8c17ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037688830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 27852988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285764, 'matching_hash': 'a1e0090e71bf48f4'}}}