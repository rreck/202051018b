```json
{
  "id": "a37325d4455dafee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290344,
  "host_pid": "9e6742732c60:1",
  "hash": "abc796a42c2824190ec44aa18b02414b07dd969a3bd0efe89e340422e4bdc638",
  "cid": "QmV1abc796a42c2824190ec44aa18b02414b07dd969a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290344,
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
      "evaluated_at": 1760290344
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
  "sig": "f0d4e143f1540185879a44654e2ba0e6932ffeed7ff9f616c066b1253e59e972"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462101683
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 49087308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': 'e66600e2d7fa312e'}}}