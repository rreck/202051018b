```json
{
  "id": "1f509f45fcc4b9bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288078,
  "host_pid": "9e6742732c60:1",
  "hash": "7a983c8fdc073fa0890807d9d52588f3049a3c8b9d14b4b0b2bab91425219914",
  "cid": "QmV17a983c8fdc073fa0890807d9d52588f3049a3c8b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288078,
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
      "evaluated_at": 1760288078
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
  "sig": "ed72abf447be238d5e6ba220a5817d3117820334c839d96fa5663d4cd6fc7f6d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 398958456380794
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 33204014, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': 'e30dc560f8e3065a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}