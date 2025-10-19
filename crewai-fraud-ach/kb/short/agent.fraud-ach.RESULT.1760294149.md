```json
{
  "id": "64a9a565a9222052",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294149,
  "host_pid": "9e6742732c60:1",
  "hash": "11a8f9055fb193229a40d934414369dd4105bd96902d70a4a3ed2ab862db3571",
  "cid": "QmV111a8f9055fb193229a40d934414369dd4105bd96",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294149,
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
      "evaluated_at": 1760294149
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
  "sig": "e0dbd5c513b44d9cdb8374d60999d2987775e7d3c466d1950230ff2a6aa6dec5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466702370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 31017008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': 'c2e86be7e57e9a06'}}}