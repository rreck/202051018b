```json
{
  "id": "2822bbada4f595c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290400,
  "host_pid": "9e6742732c60:1",
  "hash": "b16b2ba52db7749d8c0d6c1a3718317dca6ed57c66ee8f376517309dfc790d06",
  "cid": "QmV1b16b2ba52db7749d8c0d6c1a3718317dca6ed57c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290400,
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
      "evaluated_at": 1760290400
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
  "sig": "0d74fd5953dc86f2c2d5566afdeba62ff29bee353899514e5b392efd498f22b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279234721
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 34331388, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285764, 'matching_hash': 'a4a7a8ef6540eadb'}}}