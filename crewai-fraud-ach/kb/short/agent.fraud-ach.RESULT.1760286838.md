```json
{
  "id": "06bdcedaaf64cf16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286838,
  "host_pid": "9e6742732c60:1",
  "hash": "08a46ff9d5198e392e0c3f04b4d86b9f9c38ff94653ab25bcb080e7182b1184c",
  "cid": "QmV108a46ff9d5198e392e0c3f04b4d86b9f9c38ff94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286838,
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
      "evaluated_at": 1760286838
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
  "sig": "6beba23d4b1d9fdd755b5c2bf15bd95d0356cbd5896e42874ceabf70a31f28ea"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201464999191
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '0f07ea7feb264441'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '08ae7d6de60ae5f3'}}}