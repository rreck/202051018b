```json
{
  "id": "fe00a51e0fa0a440",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287846,
  "host_pid": "9e6742732c60:1",
  "hash": "8df8f5f52d2cac7371fc4e7d29fc92047705bc2d1a798a1a476de33bc5412db2",
  "cid": "QmV18df8f5f52d2cac7371fc4e7d29fc92047705bc2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287846,
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
      "evaluated_at": 1760287846
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "6d1eecdd6c56e5454a618326bd3eb263f8ccfb2088a6875487965d2f69376fb2"
}
```

Fraud detected: round_amount_pattern (score: 74)
Transaction: 031201462455734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 37000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285763, 'matching_hash': '2de7efbdf08711e2'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}