```json
{
  "id": "c5e81b3191e8b212",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293958,
  "host_pid": "9e6742732c60:1",
  "hash": "45c47cbd7f5558bb6d1203216cdaa2f7a16f98613a7a0af6a6b425537e3939c7",
  "cid": "QmV145c47cbd7f5558bb6d1203216cdaa2f7a16f9861",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293958,
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
      "evaluated_at": 1760293958
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "330cb5c4035b10591cb7e14622d58394f9a2e155b93ff6bfbff2597415cf8d8b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 398958456380794
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 92728283, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': 'e30dc560f8e3065a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}