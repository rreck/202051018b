```json
{
  "id": "94005c22ace1893d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290465,
  "host_pid": "9e6742732c60:1",
  "hash": "0135a3922f32a597d9ccae688fd8a4b493c7f9a029ed74629f95def650605a36",
  "cid": "QmV10135a3922f32a597d9ccae688fd8a4b493c7f9a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290465,
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
      "evaluated_at": 1760290465
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
  "sig": "dff0338b6a6cd7d7495a47ac5f8162035aeb9f5f4bbe4b130dcc619b434608af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461197823
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 27239645, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': 'c7e6425f6e43a399'}}}