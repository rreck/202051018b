```json
{
  "id": "03b62e2e4b5007a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292411,
  "host_pid": "9e6742732c60:1",
  "hash": "b3fe66779ed8631fd9356245f7c76f01a90ae915ee02c737599d641033cc1313",
  "cid": "QmV1b3fe66779ed8631fd9356245f7c76f01a90ae915",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292411,
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
      "evaluated_at": 1760292411
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
  "sig": "43fa8c01383becc281cd22710cb4a81c0b80f5a2744c521021cef373e273f155"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276534342
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 61495717, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': '3bb091557ce86ea6'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '304701776', 'validation_error': 'Invalid routing number checksum'}}}