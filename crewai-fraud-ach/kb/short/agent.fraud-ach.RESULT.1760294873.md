```json
{
  "id": "294249f67187c2f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294873,
  "host_pid": "9e6742732c60:1",
  "hash": "20dd46fb2514a85d92b7b6dbcf1dec27d510f2ff3c71030c4f5f466bbc3b06d9",
  "cid": "QmV120dd46fb2514a85d92b7b6dbcf1dec27d510f2ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294873,
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
      "evaluated_at": 1760294873
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
  "sig": "53cd031bb8205f0145606f8dff98cd3683b5a4dce2b0807413e630b54437c97e"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 503193792297075
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 102873264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': 'f478a6eb1bcd883b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '503193790', 'validation_error': 'Invalid routing number checksum'}}}ds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9380590}}}