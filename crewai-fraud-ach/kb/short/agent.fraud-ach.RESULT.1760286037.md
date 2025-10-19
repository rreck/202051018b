```json
{
  "id": "20dabe228051224c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286037,
  "host_pid": "9e6742732c60:1",
  "hash": "ed180fae78c14e40baf975a8294686ff62b7622308adb6bb81c95484758e7bf5",
  "cid": "QmV1ed180fae78c14e40baf975a8294686ff62b76223",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286037,
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
      "evaluated_at": 1760286037
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
  "sig": "73de837e166b4cb54ff0f1ba1d7e404f088616cacfdbde05b50e5109d0987c19"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000027276119
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285763, 'matching_hash': 'ec114b5b29b7d5ae'}}}