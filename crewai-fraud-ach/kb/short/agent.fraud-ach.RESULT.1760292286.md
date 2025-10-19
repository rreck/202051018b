```json
{
  "id": "a6007bd9e5114512",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292286,
  "host_pid": "9e6742732c60:1",
  "hash": "bdc7f2b21e69b8c7982ec64b4530ff5455e1f3745086668150e599d902cce408",
  "cid": "QmV1bdc7f2b21e69b8c7982ec64b4530ff5455e1f374",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292286,
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
      "evaluated_at": 1760292286
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
  "sig": "5e76557de7cc584e9d9518631a9e4e336e9d5540224e5aada252277cfa8426d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599696280
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 270, 'threshold': 50, 'total_amount': 64304550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 269, 'first_seen': 1760284979, 'matching_hash': '32fd26aee1bbbffc'}}}