```json
{
  "id": "b72f77492cf69c33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294456,
  "host_pid": "9e6742732c60:1",
  "hash": "b6d7d60a48c3acc8720f86897e9d2222950d872c4621c9cc78b96e400354def4",
  "cid": "QmV1b6d7d60a48c3acc8720f86897e9d2222950d872c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294456,
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
      "evaluated_at": 1760294456
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
  "sig": "59300c445df21f6686e5fcf7fce8637b304fadeb0de77ddd8b7bdbb6ca60990a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597785743
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 11900000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': 'c11d2019f761950d'}}}