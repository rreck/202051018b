```json
{
  "id": "e94f9b434929c29b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289572,
  "host_pid": "9e6742732c60:1",
  "hash": "0c2fef6f88bf6dc3f57a223d96985a1c7df284b2d69df590a7ce63f499c5e51f",
  "cid": "QmV10c2fef6f88bf6dc3f57a223d96985a1c7df284b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289572,
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
      "evaluated_at": 1760289572
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
  "sig": "6afc497a208202438f1c2c650405e0ce36b635a8f895145de26fe434b7680cd0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039514582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 40485187, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': 'c5d30db04a2c4cc4'}}}