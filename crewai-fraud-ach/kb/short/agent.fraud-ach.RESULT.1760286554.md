```json
{
  "id": "2b09a427b6d59589",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286554,
  "host_pid": "9e6742732c60:1",
  "hash": "eb5f6ca19e0598925b4007bf5a9ce0d553d4ef599e5d9ac9bd57e4f0cb1b0067",
  "cid": "QmV1eb5f6ca19e0598925b4007bf5a9ce0d553d4ef59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286554,
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
      "evaluated_at": 1760286554
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
  "sig": "8f266e42c4c8ca753af2f34411f4bd66b67b3fe6c115a59e3f3dfed09d41d4f9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249127775
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': '35c1bd481e0f1f5f'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760284979, 'matching_hash': '16ae1b567cc6df9d'}}}