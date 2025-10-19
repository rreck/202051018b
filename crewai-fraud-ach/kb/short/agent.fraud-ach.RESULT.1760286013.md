```json
{
  "id": "a960aeffb9d7352f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286013,
  "host_pid": "9e6742732c60:1",
  "hash": "115fe7e0cb2d4d26e43d676ff13fa58cb00f251668f595d2e6805c1827124cf5",
  "cid": "QmV1115fe7e0cb2d4d26e43d676ff13fa58cb00f2516",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286013,
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
      "evaluated_at": 1760286013
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
  "sig": "1f6d2ad1f65e07bd446fdcb7000963a5d582440d6b1463d794e65dd3c3038384"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100274571178
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}