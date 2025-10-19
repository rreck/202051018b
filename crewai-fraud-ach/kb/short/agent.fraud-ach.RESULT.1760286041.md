```json
{
  "id": "5ede95e8899e951c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286041,
  "host_pid": "9e6742732c60:1",
  "hash": "f8e2c2e3c8fbea3f93ae1c4863b0578140bca8e9793773a402f5e0bbd2b626c6",
  "cid": "QmV1f8e2c2e3c8fbea3f93ae1c4863b0578140bca8e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286041,
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
      "evaluated_at": 1760286041
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
  "sig": "9a98c1a1f60635c823ce6af08e2e1091d10b9b2dbf9c4a761200eb7bb4d9bec3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000031078531
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285765, 'matching_hash': '2bea5b783a868e31'}}}