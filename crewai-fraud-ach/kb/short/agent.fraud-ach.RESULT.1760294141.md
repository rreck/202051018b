```json
{
  "id": "c8b0acfa4105c7ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294141,
  "host_pid": "9e6742732c60:1",
  "hash": "1bef5d14c5865b8b3bf257085c488e02c1dc2849aeae5cb394390bd9b0ff5e2e",
  "cid": "QmV11bef5d14c5865b8b3bf257085c488e02c1dc2849",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294141,
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
      "evaluated_at": 1760294141
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
  "sig": "f5f754d4e00908bc92018716f15551e11e31f7e85112152fc8c5a1157b86e517"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155616727
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 44037080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': 'b26c49bc45dba458'}}}