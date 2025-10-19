```json
{
  "id": "d207b8f9de9125fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290973,
  "host_pid": "9e6742732c60:1",
  "hash": "ba120e03dccaa505ce8b51200e51eec8f93f4b39f89da1cd7f9a238f633167e4",
  "cid": "QmV1ba120e03dccaa505ce8b51200e51eec8f93f4b39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290973,
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
      "evaluated_at": 1760290973
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
  "sig": "4e5d2cb7db16ba3f274f1d512b81904f5ff235e242cd9d8cabaa6623687a99cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270696369
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 12316236, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': 'b3a740eac42d6623'}}}