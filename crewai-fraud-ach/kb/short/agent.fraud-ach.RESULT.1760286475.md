```json
{
  "id": "cd118caeacd1690c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286475,
  "host_pid": "9e6742732c60:1",
  "hash": "6735fb71500c06b6476dd9e42bd40fe03f58f3a0efff104415d94b0e7530d42d",
  "cid": "QmV16735fb71500c06b6476dd9e42bd40fe03f58f3a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286475,
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
      "evaluated_at": 1760286475
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "302e7967a3c910ee1c6946c733c03ed1d94b2326d65329bdcfafe0cf466a0a72"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462408143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12642058, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285765, 'matching_hash': '36407d3e627869a5'}}}