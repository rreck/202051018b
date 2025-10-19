```json
{
  "id": "f7f86aa261cd4bb4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292045,
  "host_pid": "9e6742732c60:1",
  "hash": "03296c2515b979da7c0b4203123462d985be1beec4ba98fd03ba64fe0c6fa2da",
  "cid": "QmV103296c2515b979da7c0b4203123462d985be1bee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292045,
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
      "evaluated_at": 1760292045
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
  "sig": "9a812ec562ae366251a2bb618de669a05eef730dc38c5b20eae5a64fc35bb87f"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 950960749969543
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 32809455, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': 'b177ff0c3b4ad29b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '950960749', 'validation_error': 'Invalid routing number checksum'}}}