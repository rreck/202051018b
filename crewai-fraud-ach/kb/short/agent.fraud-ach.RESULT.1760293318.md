```json
{
  "id": "16c25476f75c28b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293318,
  "host_pid": "9e6742732c60:1",
  "hash": "96e374191d6b31ef03b4a24ecfe2aef9208c805537be953fa5478d75e2b0dc04",
  "cid": "QmV196e374191d6b31ef03b4a24ecfe2aef9208c8055",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293318,
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
      "evaluated_at": 1760293318
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
  "sig": "8757964220820dc69b4eed2567c59c4a34128841448dd336ebc6cc5638c9ab22"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464396323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 22174992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': 'e47699aa17e8c37e'}}}