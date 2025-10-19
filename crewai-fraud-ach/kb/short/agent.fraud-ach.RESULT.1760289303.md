```json
{
  "id": "5c2549d2fb472964",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289303,
  "host_pid": "9e6742732c60:1",
  "hash": "2c7f687334483624345682ff7a0a2b836e5ba2ad3798dc57af04d5e00dc4fef6",
  "cid": "QmV12c7f687334483624345682ff7a0a2b836e5ba2ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289303,
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
      "evaluated_at": 1760289303
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
  "sig": "daefb7cdf1594c252718e552519b74c58f6e2e45ab1e9e5ddd4b4d4be3d8ddae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020807792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 24841369, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285764, 'matching_hash': '8390351bce6e669b'}}}