```json
{
  "id": "c3675be8bd3e0ba0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286442,
  "host_pid": "9e6742732c60:1",
  "hash": "f06b35c4cd7e45b1cf5b2dfbbd0e5896185f92a07baa5aab4da834957a6608c5",
  "cid": "QmV1f06b35c4cd7e45b1cf5b2dfbbd0e5896185f92a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286442,
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
      "evaluated_at": 1760286442
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
  "sig": "e2603fc24a8769cad963f026296273353c0674314ca089e3cabc6e79bc9f337c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105152240558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10423925, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285765, 'matching_hash': '0371944fd59dbf43'}}}