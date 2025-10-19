```json
{
  "id": "946035e4905370d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292136,
  "host_pid": "9e6742732c60:1",
  "hash": "4d571eb1a27510bd4fe40b70cd1d3f26792f31296ff74686128de4e298927b42",
  "cid": "QmV14d571eb1a27510bd4fe40b70cd1d3f26792f3129",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292136,
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
      "evaluated_at": 1760292136
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
  "sig": "6fd811cb26052085d55ad6dd7165503261b2e8a762fd9342d861f92677a5c99c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 069024451692491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 40667529, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '560f842b4bd5b95e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '069024457', 'validation_error': 'Invalid routing number checksum'}}}