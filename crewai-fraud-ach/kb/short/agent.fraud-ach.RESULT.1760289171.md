```json
{
  "id": "ca00e9d34656856c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289171,
  "host_pid": "9e6742732c60:1",
  "hash": "113647d2868c48edae6dde41a9f29ee0541a7d69a34f19387d3a0aa4799b41b5",
  "cid": "QmV1113647d2868c48edae6dde41a9f29ee0541a7d69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289171,
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
      "evaluated_at": 1760289171
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
  "sig": "b932bd0af62479893101218de21c96a185faf3cb9aa07b1c8e49503e66e0f5c4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462408143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 55916795, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285765, 'matching_hash': '36407d3e627869a5'}}}