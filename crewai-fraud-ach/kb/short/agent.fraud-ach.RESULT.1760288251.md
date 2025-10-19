```json
{
  "id": "ec156d5d94e02219",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288251,
  "host_pid": "9e6742732c60:1",
  "hash": "a989199e36d88aedfcca7d98585a485773e5b205b5649517200778b202eccffb",
  "cid": "QmV1a989199e36d88aedfcca7d98585a485773e5b205",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288251,
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
      "evaluated_at": 1760288251
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
  "sig": "d5b9ebf583e97ce8cf38f570b8186d62d0149fe58cb0e90ba549b1e091decae9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463448865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 14951211, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285765, 'matching_hash': '5a565595f8571aef'}}}