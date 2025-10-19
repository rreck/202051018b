```json
{
  "id": "79b0ddd427813f93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294488,
  "host_pid": "9e6742732c60:1",
  "hash": "f29fe87ac2d7d2643ea6df240a4a968443e0427893b7c4864f64a8a0fa23e7e8",
  "cid": "QmV1f29fe87ac2d7d2643ea6df240a4a968443e04278",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294488,
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
      "evaluated_at": 1760294488
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
  "sig": "a5ebc97a7ab22d1625bd31ca0eab352d4d9608463a16819e6da53c23364c7dbd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464999191
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 30359453, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '0f07ea7feb264441'}}}