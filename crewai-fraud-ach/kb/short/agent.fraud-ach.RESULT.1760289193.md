```json
{
  "id": "95d81dba438b3905",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289193,
  "host_pid": "9e6742732c60:1",
  "hash": "3f8731cb35056c1d7e16bee5702e7f0c1bfc2fb4bf64217129d8c5c9702d8f05",
  "cid": "QmV13f8731cb35056c1d7e16bee5702e7f0c1bfc2fb4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289193,
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
      "evaluated_at": 1760289193
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
  "sig": "222f24e9811707ad58bdad0af5b07fc13dea05a726633085d26e718c517db79e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591685004
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 38147992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': 'e63d914157ffc7ed'}}}