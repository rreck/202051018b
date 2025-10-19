```json
{
  "id": "f30ca70f531f1da8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289711,
  "host_pid": "9e6742732c60:1",
  "hash": "8994c6f71332cd375043a65d9c8eeb7f89ae2d27e51bed6f6d7d9920103273f2",
  "cid": "QmV18994c6f71332cd375043a65d9c8eeb7f89ae2d27",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289711,
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
      "evaluated_at": 1760289711
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
  "sig": "aedbd43f29a5d5ce5f9cbdbc3a0e94825efc9b7fbd487a52e0c10c4db85680ed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464854698
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 46638227, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '0df7902ca3c3b775'}}}