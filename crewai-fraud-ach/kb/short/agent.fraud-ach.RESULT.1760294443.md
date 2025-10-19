```json
{
  "id": "f8d111073a47ec7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294443,
  "host_pid": "9e6742732c60:1",
  "hash": "ea620ac35eedc21a0935dd6bd7dce58ea1a2a00ddf9ba9c65ab6dcbbdc2bf68d",
  "cid": "QmV1ea620ac35eedc21a0935dd6bd7dce58ea1a2a00d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294443,
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
      "evaluated_at": 1760294443
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
  "sig": "30dcc9ae4c1826f79507933ac0e46244d2b57e3ee07c0242a0b8d00f91911e69"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 12284846, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285764, 'matching_hash': '763c66b493018133'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}