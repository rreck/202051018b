```json
{
  "id": "37ba9edcae20dd56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290907,
  "host_pid": "9e6742732c60:1",
  "hash": "a7b77f8c6eb9c3b4ff340934e6f39fd12e7cb3669ca3a95465cf9188b13c7034",
  "cid": "QmV1a7b77f8c6eb9c3b4ff340934e6f39fd12e7cb366",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290907,
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
      "evaluated_at": 1760290907
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
  "sig": "3c3322dfc3bd0b328b4a227fc9b94783c851c0aef1659c12d89d57301db310bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029769834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 62297910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285764, 'matching_hash': '4022d05a51a758f8'}}}