```json
{
  "id": "7df41375bbac9b99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288024,
  "host_pid": "9e6742732c60:1",
  "hash": "3a2aaa6da2484a12759826090e13121ba95d134f6fde1c22f7d33ae8860538a1",
  "cid": "QmV13a2aaa6da2484a12759826090e13121ba95d134f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288024,
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
      "evaluated_at": 1760288024
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
  "sig": "05cf9c3632b7daf4b48b52fb60db59618c1097471b45054b5868d78ec96a6550"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026184073
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 24977680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285763, 'matching_hash': '5c433365b4c36f89'}}}}}