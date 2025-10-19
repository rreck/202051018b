```json
{
  "id": "a927514447bee945",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294748,
  "host_pid": "9e6742732c60:1",
  "hash": "6afd7b9291825fa7fa9a3b6c225fd4a4946b9da68d11334f26a3379e1b27496a",
  "cid": "QmV16afd7b9291825fa7fa9a3b6c225fd4a4946b9da6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294748,
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
      "evaluated_at": 1760294748
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
  "sig": "193e7d2190f936f539c175e387797abd3896932b3d10ba3d906b105bc325e596"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593273938
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 88886760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '9925ef3004078e34'}}}maly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.89, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9306664}}}