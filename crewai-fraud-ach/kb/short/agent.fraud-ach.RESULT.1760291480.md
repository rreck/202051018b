```json
{
  "id": "fe1588e926fbf767",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291480,
  "host_pid": "9e6742732c60:1",
  "hash": "acd27b1f9afaa8b71c22f29dbbe335ae0eb5f0abbe7dd9083d2fbdbb40f6ae63",
  "cid": "QmV1acd27b1f9afaa8b71c22f29dbbe335ae0eb5f0ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291480,
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
      "evaluated_at": 1760291480
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
  "sig": "c8a98166ef3de5912431708b5eff97aea9b3e9af61219c0ef8705d02b72bb1e9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150315138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 60683040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '420167e0317803c0'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '182683957', 'validation_error': 'Invalid routing number checksum'}}}