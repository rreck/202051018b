```json
{
  "id": "2d26bdcc08f06686",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286396,
  "host_pid": "9e6742732c60:1",
  "hash": "bfa3032795cba9aff6efcbe849f6d6e485c45c66281204d2f1d089f2ccf7fd01",
  "cid": "QmV1bfa3032795cba9aff6efcbe849f6d6e485c45c66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286396,
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
      "evaluated_at": 1760286396
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
  "sig": "6b574b563cd3c7540ecbcd42e5194cc666fbf97b08d82b2242fd679a4523a807"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100276179264
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': 'cb2614db0e970d70'}}}