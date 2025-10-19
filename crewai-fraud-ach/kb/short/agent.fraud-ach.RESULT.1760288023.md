```json
{
  "id": "c3a318980d0746f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288023,
  "host_pid": "9e6742732c60:1",
  "hash": "6303aa26676bf55cac8eac20f9633da4e792497ab988c2c79d823164c2355e2a",
  "cid": "QmV16303aa26676bf55cac8eac20f9633da4e792497a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288023,
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
      "evaluated_at": 1760288023
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
  "sig": "7b47a6cdeb0da251ac5db9f0273e58d1291c0e1e9ea582c3368f050838577a80"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030595065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 24309680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285763, 'matching_hash': '3889a0f66c8870f8'}}}