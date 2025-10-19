```json
{
  "id": "06096cc5ba1a9537",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292293,
  "host_pid": "9e6742732c60:1",
  "hash": "6b80b1aadea64e3c88f33a2e5797bcd5d6076d2b9e9fb0c0a83fd9a93411ae54",
  "cid": "QmV16b80b1aadea64e3c88f33a2e5797bcd5d6076d2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292293,
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
      "evaluated_at": 1760292293
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
  "sig": "95a6a5b948ada21ef1fc68b205665b3f59d3fb903cb37f09145cac921e20b0dc"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 160455148414817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 70422970, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285764, 'matching_hash': 'c57b46b00801b500'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '160455141', 'validation_error': 'Invalid routing number checksum'}}}