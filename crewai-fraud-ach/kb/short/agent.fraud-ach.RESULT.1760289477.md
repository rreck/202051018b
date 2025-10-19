```json
{
  "id": "2530a53134094759",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289477,
  "host_pid": "9e6742732c60:1",
  "hash": "54ec64cc5da9147ca16dc0c091540c196d64fc6c04116c78f3365b7121069401",
  "cid": "QmV154ec64cc5da9147ca16dc0c091540c196d64fc6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289477,
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
      "evaluated_at": 1760289477
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
  "sig": "dedfc0dc9cef0b025ff7af8811c2fbc527fc29e99a97fdf9b8817b786612f79e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 42123792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}