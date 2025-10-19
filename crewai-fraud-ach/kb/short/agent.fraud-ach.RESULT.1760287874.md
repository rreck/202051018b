```json
{
  "id": "160f2b6a2c55eb99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287874,
  "host_pid": "9e6742732c60:1",
  "hash": "36b334626921453daf25e73a12d96e0275c453fdb4303c314ba515dad3417ff2",
  "cid": "QmV136b334626921453daf25e73a12d96e0275c453fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287874,
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
      "evaluated_at": 1760287874
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
  "sig": "28df75bf46db4b23010e060c49c51acdf86e4720484844af385ec9f56a7031e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022074928
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285765, 'matching_hash': 'a87d8bfbdd334181'}}}