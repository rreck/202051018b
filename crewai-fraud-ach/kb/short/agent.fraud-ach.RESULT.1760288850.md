```json
{
  "id": "6050d290456979e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288850,
  "host_pid": "9e6742732c60:1",
  "hash": "dc6d89294cfaa07a142794fe877e6de6465e8e6994fb19e2b94e422343960674",
  "cid": "QmV1dc6d89294cfaa07a142794fe877e6de6465e8e69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288850,
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
      "evaluated_at": 1760288850
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
  "sig": "855dd8ec9c70f0634c60200ebee78c56661ed6dbc46732f07a2abdaa9f4642a8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039510138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 11895850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '4238a333ed8712d2'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}