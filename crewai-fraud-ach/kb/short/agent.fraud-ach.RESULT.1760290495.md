```json
{
  "id": "8a8443a483244865",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290495,
  "host_pid": "9e6742732c60:1",
  "hash": "e06d98d57e59893f872e4646b88ac326057444754941bd4fcfd3af3b821d7334",
  "cid": "QmV1e06d98d57e59893f872e4646b88ac32605744475",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290495,
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
      "evaluated_at": 1760290495
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
  "sig": "8c72fe69839b09cd71ca39c8de00b8707ce6144829a47447420ff37ffe679cd9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 261425243879882
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 50212744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': 'bea146cfc71ce9bb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}ds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6664302}}}