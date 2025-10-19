```json
{
  "id": "7864d341c2292be6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289199,
  "host_pid": "9e6742732c60:1",
  "hash": "ee7ca2d5ca363aaeca333b5aa82f1f4e03607794d6a5942296b42ffdc26bbbaf",
  "cid": "QmV1ee7ca2d5ca363aaeca333b5aa82f1f4e03607794",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289199,
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
      "evaluated_at": 1760289199
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
  "sig": "d08f203272101cfe51c5c443f0c26d29cf4d217cb77567e34e59594ef3f2e881"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155748621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 53907636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285764, 'matching_hash': 'df4db45348ec5c9a'}}}