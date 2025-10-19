```json
{
  "id": "b0bbae07a81f0ec3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288328,
  "host_pid": "9e6742732c60:1",
  "hash": "e3fd70616023660ce7601dc9c3eb8490ec3cb8304bf94e9c891d9e4c146b0361",
  "cid": "QmV1e3fd70616023660ce7601dc9c3eb8490ec3cb830",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288328,
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
      "evaluated_at": 1760288328
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
  "sig": "be626c4389076da9e4b3f63ad1047b84f3d987cc269843fb907cced74e6f1f1e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469479183
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 12023100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285763, 'matching_hash': '2b83b0aed5f7590d'}}}