```json
{
  "id": "26652e6a2189ae42",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289505,
  "host_pid": "9e6742732c60:1",
  "hash": "2f3add3891e2e486e30ff757054759df01c6f62cc95d26b31c882d9a867a7115",
  "cid": "QmV12f3add3891e2e486e30ff757054759df01c6f62c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289505,
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
      "evaluated_at": 1760289505
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
  "sig": "2be39cc0aac4c7d0f2955e83f8b60a930b6d09a844862a4f01f174b6e91e50fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039436848
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 56378625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '703cb1be49d2cf8f'}}}