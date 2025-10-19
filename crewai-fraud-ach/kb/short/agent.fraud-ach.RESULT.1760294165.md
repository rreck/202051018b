```json
{
  "id": "aa854e86b32e997b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294165,
  "host_pid": "9e6742732c60:1",
  "hash": "2e2f355043160403877b62ea0a0fe845052c03f59d1f5a2577469d0973c95ec3",
  "cid": "QmV12e2f355043160403877b62ea0a0fe845052c03f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294165,
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
      "evaluated_at": 1760294165
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
  "sig": "fe75900222c9af81a9a6c058bb478dff2627e24fdee8e4337fc31ce52b0d38d1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598639172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 11650000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '9f277109cf79f7ea'}}}