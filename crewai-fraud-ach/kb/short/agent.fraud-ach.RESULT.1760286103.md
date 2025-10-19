```json
{
  "id": "799f3ebe1ca54cb5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286103,
  "host_pid": "9e6742732c60:1",
  "hash": "644bf1a4c9ff929ec62106b9ebc23aec21181468eabe16364c68c61306273908",
  "cid": "QmV1644bf1a4c9ff929ec62106b9ebc23aec21181468",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286103,
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
      "evaluated_at": 1760286103
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
  "sig": "29cf8885d53e63ede998cd41372e8335650259b9eafff83b3a666c97c9ea2e20"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243970709
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}