```json
{
  "id": "1a7940054b346be2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292145,
  "host_pid": "9e6742732c60:1",
  "hash": "7d37b328a83f428efc77bd997f6fc6dc9bac9dd59e691ee1de9ac016db001965",
  "cid": "QmV17d37b328a83f428efc77bd997f6fc6dc9bac9dd5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292145,
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
      "evaluated_at": 1760292145
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
  "sig": "9bb85bba7c858c5cc04ec53752785ea7980bd04968cb49d8eb7afadaa13ae6d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460804941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 14077464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'e3b2eb0d41697d4a'}}}