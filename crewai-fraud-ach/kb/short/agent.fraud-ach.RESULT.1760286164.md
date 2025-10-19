```json
{
  "id": "82f1d452e290a22b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286164,
  "host_pid": "9e6742732c60:1",
  "hash": "a2d18e9f7c699cd8cdf4c25fe77312175b860b583516759c959ad32ffb2e862d",
  "cid": "QmV1a2d18e9f7c699cd8cdf4c25fe77312175b860b58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286164,
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
      "evaluated_at": 1760286164
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
  "sig": "e92a771d089343816a7e0f6f2905b8c7d2d17e0cf09832535a60e4cf5301ae77"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000035430994
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285765, 'matching_hash': '24f97a880bb92d0e'}}}