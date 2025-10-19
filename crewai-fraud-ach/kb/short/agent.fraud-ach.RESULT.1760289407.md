```json
{
  "id": "1c29488059e2c5dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289407,
  "host_pid": "9e6742732c60:1",
  "hash": "6980c0f735d2f3e540c24377c187905b1f7101cf4e0d87b2e1ccef9081aa5f45",
  "cid": "QmV16980c0f735d2f3e540c24377c187905b1f7101cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289407,
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
      "evaluated_at": 1760289407
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
  "sig": "583470438ed4eb20fdee7bac9be57dbc5ad6cf857deac255842224f44646149c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152430853
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 10283014, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285764, 'matching_hash': 'fa17beca2cfad33c'}}}