```json
{
  "id": "5d561034d6d495c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292788,
  "host_pid": "9e6742732c60:1",
  "hash": "26f75408a0d3421b4aac73c36bdd5b57a0ddac42018ab0cae1cc72f5b7d16a7b",
  "cid": "QmV126f75408a0d3421b4aac73c36bdd5b57a0ddac42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292788,
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
      "evaluated_at": 1760292788
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
  "sig": "d28483772dbd912c14bd2fd4a4529da84fca66600d7cb2a48b202760fded059a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246406835
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 47843105, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285764, 'matching_hash': '1c7c2a17ea2f241c'}}}