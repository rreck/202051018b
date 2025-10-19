```json
{
  "id": "b22b9743fa8a54e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288147,
  "host_pid": "9e6742732c60:1",
  "hash": "a322c9f5c469343990c484475c5770713cc6098a9d1485ac7ebbc39237fb5cbe",
  "cid": "QmV1a322c9f5c469343990c484475c5770713cc6098a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288147,
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
      "evaluated_at": 1760288147
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
  "sig": "d9ffa8e8b87d36cdb4cf66cf09bc8cf8ed4e7e61fba9889e81c90228d1cfbbc0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152345106
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 38967936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285764, 'matching_hash': '244a38e8c31df032'}}}}}