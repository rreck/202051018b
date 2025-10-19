```json
{
  "id": "40addc35bb855a5d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287430,
  "host_pid": "9e6742732c60:1",
  "hash": "7437a633c49450643dd97b3b3ee5f6a07c31c19d791b9c4a7b97256fe385e88b",
  "cid": "QmV17437a633c49450643dd97b3b3ee5f6a07c31c19d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287430,
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
      "evaluated_at": 1760287430
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
  "sig": "f218bf9dc2647563de7bb547108b6c677f85f39be044584ea990ac40798ac56b"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 987899138590267
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 26652900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285763, 'matching_hash': '4a74fde2b8c56926'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}