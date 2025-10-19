```json
{
  "id": "fd609c03ec3b73ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294223,
  "host_pid": "9e6742732c60:1",
  "hash": "88bc2a27c6fb4c683b1c6bbfb1d20a105bfa573c7e2a29ccf1ab1cd4cb277b7e",
  "cid": "QmV188bc2a27c6fb4c683b1c6bbfb1d20a105bfa573c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294223,
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
      "evaluated_at": 1760294223
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
  "sig": "bee9de83258da46cb14487f1228afb45ae1d9934f58e5cf2bc373ab6c9d24a9a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248193290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 46373184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '8925647bbeca80db'}}}