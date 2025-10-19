```json
{
  "id": "33367c58669ad13b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294428,
  "host_pid": "9e6742732c60:1",
  "hash": "68e7ba0c715cc43eb77337bda0b7897149576b8e40dee93d8dc164a6b3856f50",
  "cid": "QmV168e7ba0c715cc43eb77337bda0b7897149576b8e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294428,
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
      "evaluated_at": 1760294428
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
  "sig": "a325913c2bf0c58e7273708df594d46e089f2c4898daa5c828de5fe840e6111a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 294015856728576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 114992080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '68167a889af65895'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '294015854', 'validation_error': 'Invalid routing number checksum'}}}