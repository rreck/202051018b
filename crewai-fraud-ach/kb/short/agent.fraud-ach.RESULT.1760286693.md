```json
{
  "id": "a1b230687b6d532f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286693,
  "host_pid": "9e6742732c60:1",
  "hash": "1b385508a7a76f64a1bc88fd768a42a0676f4167bc0eace473dd1dca58156fd7",
  "cid": "QmV11b385508a7a76f64a1bc88fd768a42a0676f4167",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286693,
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
      "evaluated_at": 1760286693
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
  "sig": "d447a7cfb08941cdad3d853e8ba88b0a393dfce6c9193031579b406205aaa539"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 868351858992484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14876700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': '153716104ce1f6b1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}