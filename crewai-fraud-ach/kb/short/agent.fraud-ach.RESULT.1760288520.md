```json
{
  "id": "4f6730791df48ae7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288520,
  "host_pid": "9e6742732c60:1",
  "hash": "4b42354f9c889e37c8a4e1a1bb507001df2a8e8a471a6f20e7ed0cd191a4551b",
  "cid": "QmV14b42354f9c889e37c8a4e1a1bb507001df2a8e8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288520,
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
      "evaluated_at": 1760288520
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
  "sig": "2b67cbb51d58e17e48f9688604615c6f9d5ee64669dd0c87797cab71c7f98232"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270696369
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': 'b3a740eac42d6623'}}}