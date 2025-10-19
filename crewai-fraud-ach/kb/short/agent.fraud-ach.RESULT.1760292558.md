```json
{
  "id": "940f139597d140f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292558,
  "host_pid": "9e6742732c60:1",
  "hash": "0a9939b1b976f70d5f8b7f8eb09fbc1ae14c00ee85ef111c8d61462b342a0f77",
  "cid": "QmV10a9939b1b976f70d5f8b7f8eb09fbc1ae14c00ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292558,
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
      "evaluated_at": 1760292558
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
  "sig": "cdb2e357104ee3d8a935a4303a71e743b164c5723017ab9e6f03065c604c6a5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039436848
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 90205800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '703cb1be49d2cf8f'}}}