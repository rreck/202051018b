```json
{
  "id": "6b1cab5d12e3fbe5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288443,
  "host_pid": "9e6742732c60:1",
  "hash": "f0b79e481de23351cd5b70955866b7cc878f76e86dda86434a7894511836ae0b",
  "cid": "QmV1f0b79e481de23351cd5b70955866b7cc878f76e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288443,
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
      "evaluated_at": 1760288443
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
  "sig": "288186906ce594dd6d13c22216e836f36234d39ac024b808230369ed6dc8080a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020143117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 23250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285765, 'matching_hash': '83c798d1c8d9cfec'}}}