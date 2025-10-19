```json
{
  "id": "9910d48b6de5fdb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285701,
  "host_pid": "9e6742732c60:1",
  "hash": "cb9c6cc6b7572357a5903320766e6a31a67d818ae849b7404d25779af1a8c845",
  "cid": "QmV1cb9c6cc6b7572357a5903320766e6a31a67d818a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285701,
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
      "evaluated_at": 1760285701
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
  "sig": "2e14dfde8ecafa31691eeb97c84311d83d3a573c8a2ff0d7d2bb54f56ea15b9f"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 29918974, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}