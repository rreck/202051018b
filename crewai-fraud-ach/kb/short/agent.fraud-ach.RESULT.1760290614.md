```json
{
  "id": "23dd841e834a987b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290614,
  "host_pid": "9e6742732c60:1",
  "hash": "6acdd8533192db435c964953e2b8de2ce3f98e6fcd91a66813eeb1ca1f7e97b2",
  "cid": "QmV16acdd8533192db435c964953e2b8de2ce3f98e6f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290614,
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
      "evaluated_at": 1760290614
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
  "sig": "bced22a95ad394bfb768c9c1d239fb0ea9b95124d315f4c6d33363d1b03d4ed6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242331672
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 17934430, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '532e279550beef55'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5035466}}}