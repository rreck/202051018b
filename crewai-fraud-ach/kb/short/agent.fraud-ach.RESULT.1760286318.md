```json
{
  "id": "54d95960a7818504",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286318,
  "host_pid": "9e6742732c60:1",
  "hash": "b761d73eb9c574013fa2ba7f4e747225a932eba65b2d658fea74566fb46e8ee4",
  "cid": "QmV1b761d73eb9c574013fa2ba7f4e747225a932eba6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286318,
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
      "evaluated_at": 1760286318
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
  "sig": "922d40c23c9dc305eaaa3a355ddcd39ee46cda2013e6b582d042dbd90fad581b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105151363741
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285765, 'matching_hash': 'ec824383c23ded7d'}}}