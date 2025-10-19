```json
{
  "id": "e207dfba0d306bb3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285402,
  "host_pid": "9e6742732c60:1",
  "hash": "9d0ff71c2fb9698e53639cbcb0576448c857ab4bb4888dbcb024d9115588b195",
  "cid": "QmV19d0ff71c2fb9698e53639cbcb0576448c857ab4b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285402,
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
      "evaluated_at": 1760285402
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "26db6d505546b8c7ef3f91b4c901c3d9f6c10e971772db180bc47a6759da242c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17698548, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}