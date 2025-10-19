```json
{
  "id": "71a90a8e68adbbc8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290632,
  "host_pid": "9e6742732c60:1",
  "hash": "a8df1b2c479aa6ae0504b1b601637a9f7708fe2b0a7e3587438a830a945a40f6",
  "cid": "QmV1a8df1b2c479aa6ae0504b1b601637a9f7708fe2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290632,
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
      "evaluated_at": 1760290632
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
  "sig": "c06742b18935a0cae30cd361f07ee92ce139d18edc04fcae2ab17b8a7d18ce75"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 378944435908589
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 36354785, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '7919df3bb7d07869'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '378944430', 'validation_error': 'Invalid routing number checksum'}}}