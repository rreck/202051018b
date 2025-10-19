```json
{
  "id": "6e63c6e3085257b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294375,
  "host_pid": "9e6742732c60:1",
  "hash": "63ef72fbf0971e7184e283802b0228f47d05aa5e20bac9db8e50ad8b1fde451e",
  "cid": "QmV163ef72fbf0971e7184e283802b0228f47d05aa5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294375,
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
      "evaluated_at": 1760294375
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
  "sig": "15b90e9ab0eae8995970e4d614150b6fc917412cfcca8d87371e3b8e34b5c9d5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 667325182164908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 38907816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '7f033df851d7a625'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '667325181', 'validation_error': 'Invalid routing number checksum'}}}