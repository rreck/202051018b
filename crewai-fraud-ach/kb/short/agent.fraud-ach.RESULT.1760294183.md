```json
{
  "id": "0545bd940396652d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294183,
  "host_pid": "9e6742732c60:1",
  "hash": "ee262460b49cb9f94eedfa9c5ff1d6c2d15a233ae9e6275d715118ff1d868bd3",
  "cid": "QmV1ee262460b49cb9f94eedfa9c5ff1d6c2d15a233a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294183,
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
      "evaluated_at": 1760294183
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
  "sig": "1fc8fe66a72c0d5a03c2f898999e2c76022a40d6e60363e435787562c11c21db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033554857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 111224181, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '1f36f93e880b57ba'}}}