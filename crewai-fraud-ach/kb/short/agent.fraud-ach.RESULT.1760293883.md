```json
{
  "id": "c88c88e5b02c4bb7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293883,
  "host_pid": "9e6742732c60:1",
  "hash": "fe78851b1dc3201bc8a8cfdcd9b127aa66fbceae9133a76215c872ca435f0ba2",
  "cid": "QmV1fe78851b1dc3201bc8a8cfdcd9b127aa66fbceae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293883,
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
      "evaluated_at": 1760293883
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
  "sig": "8dee32207eaef54b46bc2e2fbb35ef711e55e1b9203525311422da8078c0b914"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 378944435908589
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 53242169, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '7919df3bb7d07869'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '378944430', 'validation_error': 'Invalid routing number checksum'}}}