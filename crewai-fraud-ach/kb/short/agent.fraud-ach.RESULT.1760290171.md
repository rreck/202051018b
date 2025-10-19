```json
{
  "id": "c7e88a2c2a17266b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290171,
  "host_pid": "9e6742732c60:1",
  "hash": "d43e349cb8628fbb34c9bffbbe127f0229256eaaef3ad685a0daa9cf97de3fa6",
  "cid": "QmV1d43e349cb8628fbb34c9bffbbe127f0229256eaa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290171,
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
      "evaluated_at": 1760290171
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
  "sig": "7a6017c78fc40487b84199d8e639e4311eeb165e1ac5cb3c76511002a47064f1"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 160455148414817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 51909715, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285764, 'matching_hash': 'c57b46b00801b500'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '160455141', 'validation_error': 'Invalid routing number checksum'}}}