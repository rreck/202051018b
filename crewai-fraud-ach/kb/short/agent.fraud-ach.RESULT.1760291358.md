```json
{
  "id": "3c56c391e3263377",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291358,
  "host_pid": "9e6742732c60:1",
  "hash": "6c7b7aeb757bc028a4d87f8a8b6fb5a5ad6f74e6d634964f2d68a2246a4bd86f",
  "cid": "QmV16c7b7aeb757bc028a4d87f8a8b6fb5a5ad6f74e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291358,
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
      "evaluated_at": 1760291358
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
  "sig": "5582e248d89c9fb8a3cc32ece71812865ad24a83fc7204c4ea7fb7b25dee2d75"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596556765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 31770412, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': '746e82f5d57aeb25'}}}