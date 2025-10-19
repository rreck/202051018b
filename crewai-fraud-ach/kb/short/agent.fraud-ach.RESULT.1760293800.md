```json
{
  "id": "b91d619503c186fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293800,
  "host_pid": "9e6742732c60:1",
  "hash": "08d18ed67251b45ad471ae9fae62b2e3be24894951e01e29291d84d50f5f441d",
  "cid": "QmV108d18ed67251b45ad471ae9fae62b2e3be248949",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293800,
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
      "evaluated_at": 1760293800
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
  "sig": "3cb57c3d23c11e32541e8e12e18ebf84edefbea9ae554ac4c0433721b836c5eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271052795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 49857408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '457d955844db0007'}}}