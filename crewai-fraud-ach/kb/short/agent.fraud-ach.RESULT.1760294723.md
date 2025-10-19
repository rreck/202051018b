```json
{
  "id": "9e3b99d9fcc41ea8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294723,
  "host_pid": "9e6742732c60:1",
  "hash": "bd475812e113d43d35f5f1f5d2c2ce9fd77a595f0c535f8f3ed37039968e27cc",
  "cid": "QmV1bd475812e113d43d35f5f1f5d2c2ce9fd77a595f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294723,
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
      "evaluated_at": 1760294723
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
  "sig": "bfd6bce3ac11f817a8a7c82d08a3af90f39f67f95514bc7d07a7bc7d890f56ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027229959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 105538545, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': 'f31e697a4f515fbb'}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '039274537', 'validation_error': 'Invalid routing number checksum'}}}