```json
{
  "id": "ebe42dcb56d2d797",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291098,
  "host_pid": "9e6742732c60:1",
  "hash": "49394f9f66a55bdca2e694dda0784568dca783f3e06e7b938d67f3978a13f4bc",
  "cid": "QmV149394f9f66a55bdca2e694dda0784568dca783f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291098,
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
      "evaluated_at": 1760291098
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
  "sig": "ea2c9ca933e37aa4c01ad3028728749ede8ea9edc078cab38f85f5fcc3d6e067"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022330150
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 73590220, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': 'b30e2736c805251a'}}}