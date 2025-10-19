```json
{
  "id": "faf6bb2a045a269a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294434,
  "host_pid": "9e6742732c60:1",
  "hash": "f9b3be0058b3d5690c1d49dfebe8bc07aad1b1c533b27f74d70de5830ec23bb9",
  "cid": "QmV1f9b3be0058b3d5690c1d49dfebe8bc07aad1b1c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294434,
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
      "evaluated_at": 1760294434
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
  "sig": "799dd8cb0b62df8f09530647749003ea8ea2cb999a0fed3e8c41a711ed3c5978"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026044300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 91466494, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '19d391c08a2c00ab'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}