```json
{
  "id": "ddc8f5a901f82a33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291609,
  "host_pid": "9e6742732c60:1",
  "hash": "7bd50d9761595dd45d6729366d7b66d4f919d89c867653915fc6fb36c07596eb",
  "cid": "QmV17bd50d9761595dd45d6729366d7b66d4f919d89c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291609,
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
      "evaluated_at": 1760291609
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
  "sig": "603bd2b35a1777158edb3d1bf6def0aa78a8e1104835ed5f7e35e1da17f09c46"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465236749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 43292403, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285764, 'matching_hash': '3442ebeb280b968f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}