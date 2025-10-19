```json
{
  "id": "8fdcd2f73a90d36a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292733,
  "host_pid": "9e6742732c60:1",
  "hash": "b96e8d0f01f7cd8fa2165072a921189bdad9a47fb10ff4365e56e1f0c6861f99",
  "cid": "QmV1b96e8d0f01f7cd8fa2165072a921189bdad9a47f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292733,
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
      "evaluated_at": 1760292733
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
  "sig": "67c4f5eae71db688a54b0ad8830bcba78f1779a9196d430df989112ad8d95d37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027960877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 66468912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '750facc395053d7c'}}}