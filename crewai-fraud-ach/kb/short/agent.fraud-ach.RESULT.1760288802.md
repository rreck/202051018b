```json
{
  "id": "d2260e3fe17863c7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288802,
  "host_pid": "9e6742732c60:1",
  "hash": "5c3cbabff62227bd3d5e73acd38fbff863542e74d5d2e397dedea88c7549e3df",
  "cid": "QmV15c3cbabff62227bd3d5e73acd38fbff863542e74",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288802,
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
      "evaluated_at": 1760288802
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
  "sig": "bd8d316b01a793aa899f57ca455e5c649ae5ef0fb64c27b2c477c795b3530b61"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 32505304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}