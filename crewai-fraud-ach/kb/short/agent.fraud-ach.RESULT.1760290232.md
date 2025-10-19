```json
{
  "id": "dc6db8489c07c095",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290232,
  "host_pid": "9e6742732c60:1",
  "hash": "cee1ebc6f7ac13fb1d75e1499ebc534c2136ad00bdc38de7e7f107c99e5689be",
  "cid": "QmV1cee1ebc6f7ac13fb1d75e1499ebc534c2136ad00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290232,
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
      "evaluated_at": 1760290232
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
  "sig": "28f20913911e3383649514b7b95daa7123345b58dd47811e39bfe830ea7e5222"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 586667912036113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 71673210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': '105f91128dc7abfc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '586667919', 'validation_error': 'Invalid routing number checksum'}}}