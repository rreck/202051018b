```json
{
  "id": "93833e1eda654e63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289269,
  "host_pid": "9e6742732c60:1",
  "hash": "c610993e7076276ced19ad0268c56e4b70ce7abff496b9eb94c0b562d8ec9a2d",
  "cid": "QmV1c610993e7076276ced19ad0268c56e4b70ce7abf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289269,
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
      "evaluated_at": 1760289269
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
  "sig": "7847117782a46eab28b6da31f1296f92616659b747e9838122927b5b265cebb2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246182467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 38158722, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285765, 'matching_hash': '281ac37534aaceb9'}}}