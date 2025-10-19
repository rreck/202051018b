```json
{
  "id": "f8fe7e2114721278",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287295,
  "host_pid": "9e6742732c60:1",
  "hash": "33ae856aada87e283a0c81f6134dc5cbdfdff9e03553698a301d34557ead8543",
  "cid": "QmV133ae856aada87e283a0c81f6134dc5cbdfdff9e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287295,
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
      "evaluated_at": 1760287295
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
  "sig": "9a4ebe28287b43979364876bf6947667605069997f4562e297c00bfd4dc14340"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201465305159
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 25087535, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285763, 'matching_hash': 'a20887ff6875d5c5'}}}