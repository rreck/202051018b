```json
{
  "id": "e9f021a7c7e1a409",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289474,
  "host_pid": "9e6742732c60:1",
  "hash": "c91ef721c764f2ba30b5b30f4f2cf7a1cca8675e65899f83c6f03bd051c5b479",
  "cid": "QmV1c91ef721c764f2ba30b5b30f4f2cf7a1cca8675e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289474,
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
      "evaluated_at": 1760289474
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
  "sig": "e18999f3d245cfb0e48f038eb856b9ec4c1e06cadedd396b8a0b399e0dd612d7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158219859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 52522556, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285765, 'matching_hash': '5fa0c304c44ad0bf'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '288759214', 'validation_error': 'Invalid routing number checksum'}}}