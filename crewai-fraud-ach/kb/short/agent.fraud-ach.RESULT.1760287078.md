```json
{
  "id": "039a5a5816c5bf10",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287078,
  "host_pid": "9e6742732c60:1",
  "hash": "8b6eba2558a0c3ae9e0c236caddf6d88bb81e2b0392fc52a6c9d29c53948de53",
  "cid": "QmV18b6eba2558a0c3ae9e0c236caddf6d88bb81e2b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287078,
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
      "evaluated_at": 1760287078
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
  "sig": "4eb494ee1c5ee4d3194d75006738a837c61f51e3d7e95beba07873d72171f4b8"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 211815510392855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15915563, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285765, 'matching_hash': '64b36e7650337f92'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '211815514', 'validation_error': 'Invalid routing number checksum'}}}