```json
{
  "id": "87bfabd9409e120d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293612,
  "host_pid": "9e6742732c60:1",
  "hash": "4836b7af2c3c5d5efc1145c9fcb0d74d561587ea5bfaee586d04a614d28c8a73",
  "cid": "QmV14836b7af2c3c5d5efc1145c9fcb0d74d561587ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293612,
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
      "evaluated_at": 1760293612
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
  "sig": "3e3e3f0f103ca6bebb2a13fe081767eb737b4a3862688c7e89c188dbac444f88"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 503193792297075
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 92836848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285764, 'matching_hash': 'f478a6eb1bcd883b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '503193790', 'validation_error': 'Invalid routing number checksum'}}}