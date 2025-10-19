```json
{
  "id": "8ad36edde1dd4a62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294342,
  "host_pid": "9e6742732c60:1",
  "hash": "830a5d99dd54fb3766187d63c6c80149211510eb3d7b5cff16201eb4257d6503",
  "cid": "QmV1830a5d99dd54fb3766187d63c6c80149211510eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294342,
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
      "evaluated_at": 1760294342
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
  "sig": "049a6b2bf59fdd6266eafa6800e5e1b7ddea3c14b23192d35e2cc4ad0837c552"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039436848
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 106442844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '703cb1be49d2cf8f'}}}