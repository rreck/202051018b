```json
{
  "id": "708c1c062c58599a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294396,
  "host_pid": "9e6742732c60:1",
  "hash": "3c496504b160e1aee7653e24d6c5383b094cf2ce1d93c66d0bdff7c60eb113a7",
  "cid": "QmV13c496504b160e1aee7653e24d6c5383b094cf2ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294396,
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
      "evaluated_at": 1760294396
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
  "sig": "9cff4367a2cbb39e613ed5115a371687dd49bea999a94b89cf10ebb20dc80451"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245569369
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 57203031, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285764, 'matching_hash': '9f2120bc546d4049'}}}