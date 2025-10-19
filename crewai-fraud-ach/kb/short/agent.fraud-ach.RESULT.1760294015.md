```json
{
  "id": "7a87b900aa5ba9b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294015,
  "host_pid": "9e6742732c60:1",
  "hash": "6f0e246b26538a56c2514cf7c4cc6c9b41eeebbb45289f59e3e70069311075c7",
  "cid": "QmV16f0e246b26538a56c2514cf7c4cc6c9b41eeebbb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294015,
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
      "evaluated_at": 1760294015
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
  "sig": "55bb7ec7b56ae9a914336256dcd724ac141ea976213973f38bfd6781edba7ad5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249758260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 84333640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '3c0efddc03414544'}}}