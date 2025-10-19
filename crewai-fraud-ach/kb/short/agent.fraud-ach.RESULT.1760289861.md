```json
{
  "id": "637f845479def1c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289861,
  "host_pid": "9e6742732c60:1",
  "hash": "69904c6bc68a53411a3f0f3f0e8d70f8ef2d3e83150d0259f0f928292e9afaa0",
  "cid": "QmV169904c6bc68a53411a3f0f3f0e8d70f8ef2d3e83",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289861,
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
      "evaluated_at": 1760289861
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
  "sig": "58b2c579160a006c0f490572b6266973d891e2a2a4ca869a6e6f5ac7738bc279"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 59358150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}