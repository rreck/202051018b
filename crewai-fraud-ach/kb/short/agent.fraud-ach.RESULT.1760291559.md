```json
{
  "id": "65dc00fcb17407de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291559,
  "host_pid": "9e6742732c60:1",
  "hash": "ce9312b5e32e40a170f7f55fa9a4592c07193d37331744c4ac26339328a32756",
  "cid": "QmV1ce9312b5e32e40a170f7f55fa9a4592c07193d37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291559,
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
      "evaluated_at": 1760291559
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
  "sig": "626558e5871d7d8f758dbb9da1a26d4a9dc13ee67f98b854e8ce42f0984b5540"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 701651307465811
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 37039130, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': '31f29b630ea434da'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}