```json
{
  "id": "a5d456882d1a351a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294298,
  "host_pid": "9e6742732c60:1",
  "hash": "c8d77589670b2831232c02a7902c79e3e31ea78beb9fe31f1486d5a7af804f77",
  "cid": "QmV1c8d77589670b2831232c02a7902c79e3e31ea78b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294298,
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
      "evaluated_at": 1760294298
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
  "sig": "e227f1ece4d37aeeff8a5de89c01dac23d29e95e91d527119ba464b31bcbffbd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 818590551241151
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 59942155, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '902b02e4e6ce46b6'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818590557', 'validation_error': 'Invalid routing number checksum'}}}