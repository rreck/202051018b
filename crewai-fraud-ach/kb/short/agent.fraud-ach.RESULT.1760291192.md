```json
{
  "id": "dc0df5420594e71e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291192,
  "host_pid": "9e6742732c60:1",
  "hash": "5521cb1094bbd36fee7d43c8068d42bca02992ee2e032ee178a60481a8a8271a",
  "cid": "QmV15521cb1094bbd36fee7d43c8068d42bca02992ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291192,
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
      "evaluated_at": 1760291192
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
  "sig": "82379ffaa4071004e548fd4653abbc5a50316eff87f77c4f954e2afb6a4cc40b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270162443
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 83998408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': 'e637274c2d5e4084'}}}