```json
{
  "id": "399738171d153aeb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292049,
  "host_pid": "9e6742732c60:1",
  "hash": "dd2422fe694f8b2df343315fce0f76470ce25ac6f6ffa2dacb8012aa917a541d",
  "cid": "QmV1dd2422fe694f8b2df343315fce0f76470ce25ac6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292049,
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
      "evaluated_at": 1760292049
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
  "sig": "2e6b9397e2d6b7dcc30b2e355a5305b9a015335a6801c6f03ab3afb2db7d0eed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463677078
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '2c78ec7dacd934fb'}}}een': 1760285763, 'matching_hash': '995d19d96715feaf'}}}