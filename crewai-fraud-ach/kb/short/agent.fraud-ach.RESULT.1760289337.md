```json
{
  "id": "8bdd44c0f8d88953",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289337,
  "host_pid": "9e6742732c60:1",
  "hash": "ff4c757704bcfe79b667959f2b16ce1d7b5c8527625f4911416eed192582fcac",
  "cid": "QmV1ff4c757704bcfe79b667959f2b16ce1d7b5c8527",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289337,
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
      "evaluated_at": 1760289337
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
  "sig": "b0eaa76bcb2b1e30d8d0553a0bb4178b85fae21b8d21034fcf2d8c99e3c23381"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 160455148414817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 43560600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285764, 'matching_hash': 'c57b46b00801b500'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '160455141', 'validation_error': 'Invalid routing number checksum'}}}