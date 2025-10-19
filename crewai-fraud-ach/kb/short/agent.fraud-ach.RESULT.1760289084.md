```json
{
  "id": "ddd12ca7297442ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289084,
  "host_pid": "9e6742732c60:1",
  "hash": "543b235525c5980304ddbc57b90db6ef738e5b663209f76af553fe7587c83be0",
  "cid": "QmV1543b235525c5980304ddbc57b90db6ef738e5b66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289084,
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
      "evaluated_at": 1760289084
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
  "sig": "a7c13020cbb2adae1471ec662dc09898580aeb0555ddb3d65f9c479606b8bd5d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463206672
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 38509722, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': 'e7b1640c0f17a3db'}}}