```json
{
  "id": "a616479d991dfa08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291720,
  "host_pid": "9e6742732c60:1",
  "hash": "a4c86b23d3c391b3b287774da983296841387683f14685fc6d5c69374dc4f2e4",
  "cid": "QmV1a4c86b23d3c391b3b287774da983296841387683",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291720,
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
      "evaluated_at": 1760291720
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
  "sig": "50d881c8337527ba2f9c86ca3fa55742557cb26285ddbe7a33f2bc4358fa86fd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 357223800655087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 30781403, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285765, 'matching_hash': '6810f1ba8ee75217'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '357223803', 'validation_error': 'Invalid routing number checksum'}}}