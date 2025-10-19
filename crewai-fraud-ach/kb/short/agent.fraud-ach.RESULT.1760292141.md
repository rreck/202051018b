```json
{
  "id": "136b94bb16c73205",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292141,
  "host_pid": "9e6742732c60:1",
  "hash": "d9f19eafcc06b7392223bcf781bd4fb6d7636939d69e324e9310798afd33fd91",
  "cid": "QmV1d9f19eafcc06b7392223bcf781bd4fb6d7636939",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292141,
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
      "evaluated_at": 1760292141
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
  "sig": "4a71e69bbe9a507e1fb2b5dae52512d282a21f442819cc378ec2dec6f20fe373"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028384993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 69805343, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285764, 'matching_hash': '07aae5a269425bd8'}}}