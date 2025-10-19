```json
{
  "id": "3b92e260413a5aa1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293975,
  "host_pid": "9e6742732c60:1",
  "hash": "108b6caaf3f5eee94ed39f679b9c70405fa44e426a2a9c3ce0ead50578d49d94",
  "cid": "QmV1108b6caaf3f5eee94ed39f679b9c70405fa44e42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293975,
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
      "evaluated_at": 1760293975
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
  "sig": "6af304880fbd42e3c136e8796204c7bc3c688da451dc8b928459094e6f7e202e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276997857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 108946063, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': 'b73e9a6de72cc131'}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}