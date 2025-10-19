```json
{
  "id": "a383e37b583689b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289184,
  "host_pid": "9e6742732c60:1",
  "hash": "739f0625920dd150453a0bca1616b4dfdbcb3f45ce140f724bc3b348fe21bbf7",
  "cid": "QmV1739f0625920dd150453a0bca1616b4dfdbcb3f45",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289184,
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
      "evaluated_at": 1760289184
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
  "sig": "534d9f2f266e1306ab9eb1b3151dfdf69d198f41ef94740b67ad460890d0b185"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593402675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 25279068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '1478dad6bc2a5e7e'}}}