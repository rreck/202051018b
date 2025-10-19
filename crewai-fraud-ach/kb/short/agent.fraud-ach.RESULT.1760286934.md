```json
{
  "id": "a908978c56cbffac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286934,
  "host_pid": "9e6742732c60:1",
  "hash": "61c5a0d93bd91699f7211fc86ac968d3ac31cc4a6cfa0793fc4b249a0c368520",
  "cid": "QmV161c5a0d93bd91699f7211fc86ac968d3ac31cc4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286934,
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
      "evaluated_at": 1760286934
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
  "sig": "2591cae63e881474fd9227cc95fc28d12e0b5329fc1c448a3b0c3204cbcb9941"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 160455148414817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15246210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285764, 'matching_hash': 'c57b46b00801b500'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '160455141', 'validation_error': 'Invalid routing number checksum'}}}