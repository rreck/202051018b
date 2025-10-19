```json
{
  "id": "2f4afe79d43db3f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291607,
  "host_pid": "9e6742732c60:1",
  "hash": "04c997bb657af0bbf10d839b8c79aa73f2e2a38c796d15fb971d1dd6a08842ef",
  "cid": "QmV104c997bb657af0bbf10d839b8c79aa73f2e2a38c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291607,
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
      "evaluated_at": 1760291608
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
  "sig": "9e1b37d68999a8899f8a4817affce463d9a7dd9f5193280c95dc2d78056854c7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039510138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 20088275, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': '4238a333ed8712d2'}}}