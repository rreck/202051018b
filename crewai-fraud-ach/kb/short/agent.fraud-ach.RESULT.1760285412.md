```json
{
  "id": "092ec66fd21b3b02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285412,
  "host_pid": "9e6742732c60:1",
  "hash": "96685ac5fdc8b70364ed292bed7caee116c10212d80190a0ccb882375dce1977",
  "cid": "QmV196685ac5fdc8b70364ed292bed7caee116c10212",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285412,
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
      "evaluated_at": 1760285412
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
  "sig": "dc3c7cc84237230a13430a0bdf646864050d0cd59e22cf669e548fd55e4b8878"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18119942, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}