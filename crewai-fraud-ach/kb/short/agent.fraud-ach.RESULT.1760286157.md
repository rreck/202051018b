```json
{
  "id": "62855cf8d64f8982",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286157,
  "host_pid": "9e6742732c60:1",
  "hash": "55f56157783a1c513a816beecdc957399b6e684f5947f3a55706506c37ade0ef",
  "cid": "QmV155f56157783a1c513a816beecdc957399b6e684f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286157,
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
      "evaluated_at": 1760286157
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
  "sig": "6aed773e6ca66672eda8b435cb53ae6ac86a117a59ea4886d21fcc479aea534d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105155616727
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285765, 'matching_hash': 'b26c49bc45dba458'}}}