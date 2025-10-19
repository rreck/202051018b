```json
{
  "id": "05f78fb271444099",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294916,
  "host_pid": "9e6742732c60:1",
  "hash": "dfa2776ae7d53e456a27e56b5d0010080f2e6a186eeb048eef7011ff04308510",
  "cid": "QmV1dfa2776ae7d53e456a27e56b5d0010080f2e6a18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294916,
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
      "evaluated_at": 1760294916
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
  "sig": "a51a2c9b1ac715c02255de4f5ff1d111b2b6022f682b764747a6279127bd5275"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 864091464204372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 58444893, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '74f25dd839f89a8f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}