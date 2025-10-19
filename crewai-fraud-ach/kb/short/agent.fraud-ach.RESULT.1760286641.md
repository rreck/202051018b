```json
{
  "id": "1c2cc7d43263eaa0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286641,
  "host_pid": "9e6742732c60:1",
  "hash": "8a9a0055c09bdd34fa1c812a4370ab81369d9466eadc98a6fb41694671d4b3f3",
  "cid": "QmV18a9a0055c09bdd34fa1c812a4370ab81369d9466",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286641,
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
      "evaluated_at": 1760286641
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
  "sig": "a836efc591209182605ffa6354aa35969bcaf6d36987cf38d91c39cc9e7b42f9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249454336
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285763, 'matching_hash': '6b4cd9d1923f5d4e'}}}