```json
{
  "id": "f81f6f53370cb0f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287871,
  "host_pid": "9e6742732c60:1",
  "hash": "0e4a84eb22052b38a9f9885d936efec16934efce400748399a894d15e5e9e637",
  "cid": "QmV10e4a84eb22052b38a9f9885d936efec16934efce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287871,
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
      "evaluated_at": 1760287871
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
  "sig": "98f2524901bdbc5dd69290c8f9ec22c69fa292ff91ba29eeb9a8a3f3442eed42"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 834096557545062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 25451250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285764, 'matching_hash': 'c4c3f7a3fe4b8b75'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '834096558', 'validation_error': 'Invalid routing number checksum'}}}